#include<stdio.h>
#include<algorithm>
#include<string.h>
#define rep(ii,a,b) for (int ii=(a);ii<=(b);ii++)
#define rek(ii,a,b) for (int ii=(a);ii>=(b);ii--)
using namespace std;
int test,n,ans;
bool v[20];
void deal(int n)
{
    int t=n;
    while(t)
    {
        v[t%10]=1;
        t/=10;
    }
}
bool check()
{
    rep(i,0,9) if (!v[i]) return true;
    return false;
}
int main()
{
    //freopen("ainput.in","r",stdin);
    //freopen("aoutput.out","w",stdout);
    scanf("%d",&test);
    rep(ii,1,test)
    {
        scanf("%d",&n);
        if (n==0) printf("Case #%d: INSOMNIA\n",ii);
            else {
                ans=1;
                rep(i,0,9) v[i]=0;
                deal(n);
                ans=n;
                for (int i=2;check();i++)
                {
                    deal(i*n);
                    ans=i*n;
                }
                printf("Case #%d: %d\n",ii,ans);
            }
    }

    return 0;
}
