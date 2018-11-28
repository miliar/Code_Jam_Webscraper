//OUM HARI OUM, OUM TATSAT
// OUM NAMA VAGABATE BASUDEBAY
// OUM NAMA MA SWARASATI OUM NAMA

#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

#define sc1(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d %d",&a,&b)
#define sc3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define scd1(a) scanf("%lf",&a)
#define scd2(a,b) scanf("%lf %lf",&a,&b)
#define scd3(a,b,c) scanf("%lf %lf %lf",&a,&b,&c)
#define scl1(a) scanf("%lld",&a)
#define scl2(a,b) scanf("%lld %lld",&a,&b)
#define scl3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
//#define scl1(a) scanf("%I64d",&a)
//#define scl2(a,b) scanf("%I64d %I64d",&a,&b)
//#define scl3(a,b,c) scanf("%I64d %I64d %I64d",&a,&b,&c)


#define cl(vctr) vctr.clear()
#define ms(v, ar) memset(ar, v, sizeof(ar))

const double pi=(double)(2.0 * acos( 0.0 ));
const int inf=1 << 30;
const double eps=1E-9;
const double e = exp(1.0);
const int sz=100000 + 5;

using namespace std;
typedef long long int ll;
const ll mod=1000000000 + 7;

char s[sz];
bool cnt[sz];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, T;
    sc1(t); T=t;
    while(t--)
    {
        int k;
        scanf("%s %d", &s, &k);
        int l = strlen(s);
        for(int i=0; i<l; i++)
            cnt[i] = s[i]=='+' ? 1 : 0;

        int res=0;
        for(int i=0; i+k-1<l; i++)
        {
            if(!cnt[i])
            {
                for(int j=0; j<k; j++)
                    cnt[i+j]^=1;
                res++;
            }
        }

        printf("Case #%d: ", T-t);

        bool ch =1;
        for(int i=0; i<l && ch; i++)
            if(!cnt[i])
                ch=0;
        if(!ch)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", res);
    }

    return 0;
}

























