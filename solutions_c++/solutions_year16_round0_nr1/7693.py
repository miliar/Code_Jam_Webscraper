/*

ID: jbsu321
PROG: test
LANG: C++

*/

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
#define ll int
#define ff float
#define MP make_pair
#define EPS 10E-10
#define fr first
#define sc second
#define MAXX 100
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
#define csprint printf("Case %lld: ", C++)
#define bpc __builtin_popcount

#define REP(i,N)  for(i=0;i<N;i++)
#define REV(i,N)  for(i=N;i>=0;i--)
#define FOR(i,p,k) for (i=p; i<k;i++)


#define ISS         istringstream
#define OSS         ostringstream
#define VS          vector<string>
#define vi          vector<int>
#define vd          vector<double>
#define vll         vector<long long>
#define SII         set<int>::iterator
#define SI          set<int>
#define mem(a,b)    memset(a,b,sizeof(a))
#define fs          first
#define sc          second
#define pii         pair < int , int >

#define EQ(a,b)     (fabs(a-b)<ERR)


#define FORE(i,a)   for(typeof((a).begin())i=(a).begin();i!=(a).end();i++)

#define round(i,a)  i = ( a < 0 ) ? a - 0.5 : a + 0.5;
#define makeint(n,s)  istringstream(s)>>n
#define read()      freopen("test.txt","r",stdin)

using namespace std;

//ll Pow(ll B,ll P){      ll R=1; while(P>0)      {if(P%2==1)     R=(R*B);P/=2;B=(B*B);}return R;}
//ll Gcd(ll a,ll b){ if(b==0)return a; Gcd(b,a%b); return;}

///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

//ll fact[] = {1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000,20922789888000,355687428096000,6402373705728000,121645100408832000,2432902008176640000};

//void factorial(ll mm){fact[0]=fact[1]=1;fact[2]=2;for(int i=3; i<1001; i++)fact[i]=(i*fact[i-1])%mm;}

//9,9+90*2,9+90*2+900*3,9+90*2+900*3+9000*4,9+90*2+900*3+9000*4+90000*5,9+90*2+900*3+9000*4+90000*5+900000*6,9+90*2+900*3+9000*4+90000*5+900000*6+9000000*7,9+90*2+900*3+9000*4+90000*5+900000*6+9000000*7+90000000*8
//ll arrToNumberOfDigits[]={9,9+90*2,9+90*2+900*3,9+90*2+900*3+9000*4,9+90*2+900*3+9000*4+90000*5,9+90*2+900*3+9000*4+90000*5+900000*6,9+90*2+900*3+9000*4+90000*5+900000*6+9000000*7,9+90*2+900*3+9000*4+90000*5+900000*6+9000000*7+90000000*8};

//int loop1[]={1,1,1,0,0,-1,-1,-1};
//int loop2[]={-1,0,1,-1,1,1,0,-1};

//pall MV(ll a, ll b, ll c, ll d){pall aa;aa.fr=c-a;aa.sc=d-b;return aa;}
//ll CP(ll a, ll b, ll c, ll d){return (a*d-b*c);}

void process()
{
    ll T, n, C=1, temp, x;
    bool bit_check[10], flag;
    cin>>T;
    while(T--){
        ms(bit_check, false);
        cin>>n;
        cout<<"Case #"<<C++<<": ";
        for(int i=1; i<=10000; i++){
            temp = n*i;
            while(temp){
                x = temp%10;
                bit_check[x]=true;
                temp/=10;
            }
            flag = true;
            for(int i=0; i<10; i++){
                if(!bit_check[i]){
                    flag=false;
                    break;
                }
            }
            if(flag){
                //cout<<n<<" "<<i<<" ";
                cout<<n*i<<endl;
                //cout<<"???";
                break;
            }
            else if(!flag and i==1000){
                cout<<"INSOMNIA"<<endl;
            }
        }
    }
	return;
}

int main()
{
    freopen("Al.txt","r",stdin);
    freopen("output.txt","w",stdout);

    process();
    return 0;
}




















