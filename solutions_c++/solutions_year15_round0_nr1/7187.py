#include<bits/stdc++.h>
using namespace std;
char s[1005];
int main()
{
    #ifndef ONLINE_JUDGE
freopen("input.txt","r",stdin);
freopen("ouput.txt","w",stdout);
#endif
    int t,n,j=1;
    cin>>t;
   for(j=1;j<=t;j++)
    {
        int f=t;
        cin>>n;
        scanf("%s",s);
        int finalans=0;
        int people=0;
        people=(s[0]-'0');
        for(int i=1;i<=n;i++)
        {
                if(people<i)
                {
                    finalans+=i-people;
                    people+=(i-people);
                }
                people+=(s[i]-'0');
        }
        printf("Case #%d: %d\n",j,finalans);
    }
}
