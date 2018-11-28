#include <iostream>
#include <cstdio>
using namespace std;
int T,ind,moves;
string s;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    //freopen("DATA.txt","r",stdin);
    scanf("%i",&T);
    for (int t=1;t<=T;t++)
    {
        moves=0;
        cin>>s;
        while (!s.empty())
        {
            while (!s.empty() && s[s.length()-1]=='+')
            {
                s=s.erase(s.length()-1);
            }
            if (s.empty())continue;
            if (s[0]=='-')
            {
                for (int i=0;i<s.length();i++)
                {
                    if (s[i]=='+')s[i]='-';
                    else s[i]='+';
                }
                for (int i=0;i<s.length()/2;i++)
                {
                    swap(s[i],s[s.length()-i-1]);
                }
            }
            else
            {
                for (int i=0;i<s.length();i++)
                {
                    if (s[i]=='+')s[i]='-';
                    else break;
                }
            }
            moves++;
        }
        printf("Case #%i: %i\n",t,moves);
    }
}
