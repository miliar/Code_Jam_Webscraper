                          /* *******RAHUL MORE********
                             *****N.I.T. DURGAPUR***** */


#include<bits/stdc++.h>

#define ll long long
#define l long

#define ins(s) scanf("%s",s)
#define in(s) scanf("%d",&s)
#define inc(s) scanf("%c",&s)
#define inl(s) scanf("%ld",&s)
#define inll(s) scanf("%lld",&s)
#define outs(s) printf("%s\n",s)
#define out(s) printf("%d\n",s)
#define outc(s) printf("%c\n",s)
#define outl(s) printf("%ld\n",s)
#define outll(s) printf("%lld\n",s)
#define lp(i,a,n)  for(i=a;i<n;i++)
#define mal(n) (int*)malloc(sizeof(int)*n)
#define mem(a) memset(a,0,sizeof(a))
#define gc getchar
#define pc putchar
#define md 1000000007
using namespace std;

int main()
{
    freopen("tst.c","r",stdin);
    freopen("tst1.c","w",stdout);
int st_aud,ans,diff,i,j,t,max_shy;
char st[1005];
in(t);
lp(j,0,t)
{
    diff=0;ans=0;st_aud=0;
    in(max_shy);
    ins(st);
    for(i=0;i<=max_shy;i++)
    {
        if(st_aud>=i)
        {
            st_aud += st[i]-'0';
            continue;
        }
        else
        {
            diff = i-st_aud;
            ans += diff;
            st_aud += diff + st[i]-'0';
        }
    }
    printf("Case #%d: %d\n",j+1,ans);
}

return 0;
}
