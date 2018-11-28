#include<bits/stdc++.h>
#define PB(u)  push_back(u)
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
using namespace std ;
#define MAX 100005
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);
const int mod=1e9+7;

char s[1005];

char flip(char a)
{
    if(a=='-') return '+';
    else return '-';
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int k;
        scanf(" %s %d",s+1,&k);
        bool ok=1;
        int ans=0;
        int n =strlen(s+1);
        for(int i=1;i<=n;i++)
        {
            if(s[i]=='-')
            {
                if(n-i+1<k)
                {
                    ok=0;
                    break;
                }
                else
                {
                    for(int j=0;j<k;j++)
                        s[i+j]=flip(s[i+j]);
                    ans++;
                }
            }
        }
        printf("Case #%d: ",cas++);
        if(ok)
            printf("%d\n",ans);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0 ;
}

