#include<bits/stdc++.h>
#define MOD 1000000007
#define MX 100010
#define ll long long
#define sc(n) scanf("%d",&n)
#define pr(m) printf("%d\n",m)
#define pi acos(-1.0)

using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2large.txt","w",stdout);
    int t,tc=1,i;
    sc(t);
    char a[105];
    while(t--)
    {
        int con=0;
        scanf("%s",a);
        int l=strlen(a);
        for(i=l-1;i>=0;i--){
            if(a[i]=='-'){
                con++;
                for(int j=0;j<=i;j++){
                    if(a[j]=='-')a[j]='+';
                    else a[j]='-';
                }
            }
        }
        printf("Case #%d: %d\n",tc++,con);
    }

    return 0;
}
