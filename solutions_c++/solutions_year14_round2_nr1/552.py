#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>


using namespace std;

ifstream in("large_A.in");
ofstream out("large_A.out");

int main()
{
	int test, t, n;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
        in >> n;
        vector <string> v(n);
        vector <int> index(n);
        for (int i = 0; i < n; ++i)
        {
            in >> v[i];
            index[i] = 0;
        }
        long long patasxan = 0;
        bool pat = true;
        while (index[0] < v[0].size() && pat)
        {
            vector <int> tiv;
            vector <char> ch;
            for (int i = 0; i < n; ++i)
            {
                int k = index[i], count = 0;
                while (k < v[i].size() && v[i][k] == v[i][index[i]])
                {
                    k++;
                    count++;
                }
                ch.push_back(v[i][index[i]]);
                index[i] = k;
                tiv.push_back(count);
            }
            long long answer = -1;
            for (int g = 0; g < 101; ++g)
            {
                int ans = 0;
                for (int i = 0; i < tiv.size(); ++i)
                    ans += abs(tiv[i] - g);
                if (ans < answer || answer == -1)
                    answer = ans;
            }
            patasxan += answer;

            for (int i = 0; i < ch.size(); ++i)
                if (ch[i] != ch[0])                
                    pat = false;
        }

        for (int i = 0; i < n; ++i)
            if (index[i] < v[i].size())
                pat = false;

        if (pat)
            out << "Case #" << t << ": " << patasxan << endl;
        else
            out << "Case #" << t << ": Fegla Won" << endl;
    }

	return 0;
}