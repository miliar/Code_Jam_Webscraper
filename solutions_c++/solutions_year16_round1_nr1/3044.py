#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("CJ_R1A_1","w",stdout);
    int t,cou=1;
    scanf("%d",&t);
    while(t--)
    {
        string s;
        cin>>s;
        int n=s.length(),i;
        string u;
        u[0]=s[0];
        for(i=0;i<n;i++)
        {
            if(s[i]>=u[0])
            {
                u=s[i]+u;
            }
            else
            {
                u=u+s[i];
            }
        }
        printf("Case #%d: ",cou);
        cout<<u<<endl;
        cou++;
    }
return 0;
}
