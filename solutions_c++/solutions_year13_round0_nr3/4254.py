/// BIS-MILLAHIR RAHMANIR RAHIM

#include<algorithm>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<deque>
#include<climits>

using namespace std;

#define all(a) a.begin(),a.end()
#define I1(n) scanf("%d",&n)
#define I2(n1,n2) scanf("%d%d",&n1,&n2)
#define I3(n1,n2,n3) scanf("%d%d%d",&n1,&n2,&n3)
#define F(i, a, b) for(  i = (a); i <= (b); i++ )
#define FR(i, a, b) for(  i = (a); i < (b); i++ )
#define FRR(i, a, b) for(  i = (a); i >b; i-- )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Pr(x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++) cout << *it << " "; cout << endl;
#define pb push_back
#define pi acos(-1.0)
#define MEM(a,val) memset(a,val,sizeof(a))
#define eps 1e-9
#define Max(a,b) (a>b?a:b)
#define Min(a,b) (a<b?a:b)
#define sz(a) ((int)(a).size())
#define IN  freopen("input.txt","r",stdin)
#define OUT freopen("output.txt","w",stdout)
#define CLR(n) n.clear()
#define SQR(n) (n*n)
#define LEFT (idx<<1)
#define RIGHT (LEFT+1)

template<typename T> T POW(T B,T P){ if(P==0) return 1; if(P&1) return B*POW(B,P-1);  else return SQR(POW(B,P/2));}


int main()
{

    freopen("C-large-1.in","r",stdin);
    OUT;

    int tc,cas=1;

    long long a,b,i,cnt,lim;

    map<int,bool>MP;


    vector<long long int>v(50);


v[0] = 1;
v[1] = 4;
v[2] = 9;
v[3] = 121;
v[4] = 484;
v[5] = 10201;
v[6] = 12321;
v[7] = 14641;
v[8] = 40804;
v[9] = 44944;
v[10] = 1002001;
v[11] = 1234321;
v[12] = 4008004;
v[13] = 100020001;
v[14] = 102030201;
v[15] = 104060401;
v[16] = 121242121;
v[17] = 123454321;
v[18] = 125686521;
v[19] = 400080004;
v[20] = 404090404;
v[21] = 10000200001;
v[22] = 10221412201;
v[23] = 12102420121;
v[24] = 12345654321;
v[25] = 40000800004;
v[26] = 1000002000001;
v[27] = 1002003002001;
v[28] = 1004006004001;
v[29] = 1020304030201;
v[30] = 1022325232201;
v[31] = 1024348434201;
v[32] = 1210024200121;
v[33] = 1212225222121;
v[34] = 1214428244121;
v[35] = 1232346432321;
v[36] = 1234567654321;
v[37] = 4000008000004;
v[38] = 4004009004004;



    I1(tc);

    while(tc--)
    {
        scanf("%lld %lld",&a,&b);

        cnt = 0;

        for(i=0;i<39;i++)
            if(v[i]>=a && v[i]<=b) cnt++;

        printf("Case #%d: %lld\n",cas++,cnt);
    }


    return 0;
}
