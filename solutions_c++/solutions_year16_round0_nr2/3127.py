#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    int curCase=1;
    while(t--)
    {
        string s;
        cin>>s;
        int sol=0;
        for(int i=s.length()-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                for(int j=0;j<=i;j++)
                    if(s[j]=='+')s[j]='-';
                    else s[j]='+';
                for(int j=0;j<=i;j++)
                    swap(s[j],s[i-j]);
                sol++;
            }
        }
        printf("Case #%d: %d\n",curCase,sol);
        curCase++;
    }
    return 0;
}
