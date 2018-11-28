#include <bits/stdc++.h>

using namespace std;
int T;
string N[101];
bool isHappy(int i)
{
    for(int _i = 0; _i<N[i].size(); _i++)
    {
        if(N[i][_i]=='-') return false;
    }
    return true;
}
int main()
{
    ofstream file ("output.out");
    int i,j;
    cin>>T;
    for(i=0; i<T; i++)
    {
        cin>>N[i];
    }
    for(i=0; i<T; i++)
    {
        /// /// ///

        if(isHappy(i))
        {
            file<<"Case #"<<i+1<<": "<<0<<endl;
            continue;
        }

        int lastMinus;
        int tries=0;
        while(!isHappy(i))
        {
            tries++;
            for(j=N[i].size()-1; j>=0; j--)
            {
                if(N[i][j]=='-')
                {
                    lastMinus=j;
                    break;
                }
            }
            for(j=0; j<=lastMinus; j++)
            {
                if(N[i][j]=='+') N[i][j]='-';
                else N[i][j]='+';
            }
        }
        file<<"Case #"<<i+1<<": "<<tries<<endl;
        /// /// ///
    }
    return 0;
}
