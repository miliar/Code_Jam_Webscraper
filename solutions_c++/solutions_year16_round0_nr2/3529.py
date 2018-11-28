#include<bits/stdc++.h>
using namespace std;
#define MAX 1000001
typedef long long ll;

int main()
{
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t; IF >> t;
    for(int tt=1;tt<=t;tt++)
    {
        string s; IF >> s;
        int dp[110]={0};
        if(s[0]=='-')
            dp[1]=1;
        int l = s.size();
        for(int i=1;i<l;i++)
        {
            if(s[i]=='+')
                dp[i+1] = dp[i];
            else
            {
                int j=i-1;
                while(s[j]=='-' && j>=0)
                    j--;
                if(j==-1)
                    dp[i+1] = 1;
                else
                    dp[i+1] = 2 + dp[j];
            }
        }
        OF << "Case #" << tt << ": " << dp[l] << endl;
    }
    OF.close(); IF.close();
}
