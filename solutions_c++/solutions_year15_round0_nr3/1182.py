#include <iostream>
#include <fstream>

using namespace std;

ofstream fout("output2.txt");

typedef pair<char, int> Quatern;

Quatern product(Quatern &a, Quatern& b)
{
    Quatern answer;
    
    answer.second = a.second * b.second;
    answer.first = '1';
    
    if (a.first == '1')
    {
        answer.first = b.first;
        return answer;
    }
    if (b.first == '1')
    {
        answer.first = a.first;
        return answer;
    }

    if (a.first == b.first)
    {
        answer.second *= -1;
        answer.first = '1';
        return answer;
    }

    if (a.first == 'i')
        if (b.first == 'j')
            answer.first = 'k';
        else
        {
            answer.first = 'j';
            answer.second *= -1;
        }
    
    if (a.first == 'j')
        if (b.first == 'k')
            answer.first = 'i';
        else
        {
            answer.first = 'k';
            answer.second *= -1;
        }
    
    if (a.first == 'k')
        if (b.first == 'i')
            answer.first = 'j';
        else
        {
            answer.first = 'i';
            answer.second *= -1;
        }

    return answer;
}

int main()
{
    int T;
    Quatern Q_i = make_pair('i', 1), Q_j = make_pair('j', 1), Q_k = make_pair('k', 1);
    Quatern Q_ij = product(Q_i, Q_j);
    string equation;
    long long L, X;

    cin >> T;	
    for (int t = 0; t < T; ++t)
    {
        cin >> L >> X;   
        cin >> equation;

        bool has_i = false, has_j = false;
        long long Y = (X <= 6) ? X: 4 + X % 4;
        Quatern part = make_pair('1', 1);
        string answer = "NO";
        
        
        for (int i = 0; i < Y; ++i)
        {
            for (int j = 0; j < equation.size(); ++j)
            {
                if (equation[j] == 'i')
                    part = product(part, Q_i);

                if (equation[j] == 'j')
                    part = product(part, Q_j);
                
                if (equation[j] == 'k')
                    part = product(part, Q_k);

                if (has_i == true && part == Q_ij)
                    has_j = true;

                if (part == Q_i)
                    has_i = true;
            }
        }
        
        if (part == make_pair('1', -1) && has_i && has_j)
            answer = "YES";

        fout << "Case #" << t + 1 << ": " << answer << endl;
    }
	return 0;
}