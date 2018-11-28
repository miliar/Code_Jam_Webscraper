#include <string>
#include <fstream>
#include <iostream>
using namespace std;

int to_pos(string, int);

int to_neg(string S, int n)
{
    if(n < 0)
        return 0;
        
    if(S[n] == '+')
    {
        int pos = to_pos(S, n - 1);
        int neg = to_neg(S, n - 1);
        
        if(pos <= neg + 1)
            return pos + 1;
        return neg + 2;
    }
    else
    {
        int pos = to_pos(S, n - 1);
        int neg = to_neg(S, n - 1);
        
        if(neg <= pos + 1)
            return neg;
        return pos + 1;
    }
}

int to_pos(string S, int n)
{
    if(n < 0)
        return 0;
        
    if(S[n] == '+')
    {
        int pos = to_pos(S, n - 1);
        int neg = to_neg(S, n - 1);
        
        if(pos <= neg + 1)
            return pos;
        return neg + 1;
    }
    else
    {
        int pos = to_pos(S, n - 1);
        int neg = to_neg(S, n - 1);
        
        if(neg <= pos + 1)
            return neg + 1;
        return pos + 2;
    }
}

int main()
{
    ifstream fin("B-small-attempt0.in");
    ofstream fout("B.txt");
    
    int T;
    fin >> T;
    for(int t = 1; t <= T; ++t)
    {
        string S;
        fin >> S;
        
        fout << "Case #" << t << ": " << to_pos(S, S.length() - 1) << endl;
    }
    
    return 0;
}
