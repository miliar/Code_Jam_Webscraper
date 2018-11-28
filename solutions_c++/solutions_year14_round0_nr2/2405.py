
/*
   ______    _____
        |    |    \
        |    |     \
        |    |_____/
   \-   |    |     \
    \  /     |     /
     \/      |____/


*/


/*Mes que un equipe*/

//জিষ্ণু ব্যানার্জী
//একজন পরিত্যাক্ত কোডার
//জীবনের কারাগারে আজীবন সাজাপ্রাপ্ত একজন আসামী


#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <list>
#include <bitset>
#include <ctime>

#define ms(a,b) memset(a, b, sizeof(a))
#define pb(a) push_back(a)
#define pi (2*acos(0))
#define oo 1<<29
#define dd double
#define ll long long
#define ff float
#define MP make_pair
#define ERR 10E-7
#define fr first
#define sc second
#define SZ(a) (int)a.size()
#define all(a) a.begin(),a.end()

#define intlim 2147483648
#define rtintlim 46340
#define llim 9223372036854775808
#define rtllim 3037000499

#define pall pair<ll,ll>
#define padd pair<dd,dd>
#define paii pair<int,int>
#define ull unsigned long long
#define csprint printf("Case %lld:\n", C++)
#define bpc __builtin_popcount
#define EQ(a,b)     (fabs(a-b)<ERR)
#define fast_input_output ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

//ll Pow(ll B,ll P){      ll R=1; while(P>0)      {if(P%2==1)     R=(R*B);P/=2;B=(B*B);}return R;}
//int BigMod(ll B,ll P,ll M){     ll R=1; while(P>0)      {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;} /// (B^P)%M
//ll Gcd(ll a,ll b){ if(b==0)return a; Gcd(b,a%b); return;}

///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

//ll fact[] = {1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000,20922789888000,355687428096000,6402373705728000,121645100408832000,2432902008176640000};

#define max_x 1010
#define max_y 1010

ll T;
int C=1, N;

void process()
{
    cin>>T;
    while(T--)
    {
        dd company_price, extra_rate , to_win;
        cin>>company_price>>extra_rate>>to_win;
//        cout<<"Case #"<<C++<<": ";
        printf("Case #%d: ",C++);
        dd value = 2000000000.0;
        for(int number=0; ; number++)
        {
            dd time = 0.0;
            for(int i=0; i<number; i++)
            {
                time = time + (company_price/(2.0+(extra_rate*i)));
            }
            time = time + ( to_win/(2.0+number*extra_rate) );
            if(time < value)
            {
                value = time;
            }
            else break;
        }
        printf("%.7lf\n", value);
    }
    return;
}

int main()
{
    fast_input_output
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    process();
    return 0;
}
