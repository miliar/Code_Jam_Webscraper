#include <bits/stdc++.h>

#ifdef LOCAL_BUILD
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif

typedef long long LL;
typedef unsigned long long ULL;
typedef int  I32;
typedef unsigned int  UI32;
typedef short I16;
typedef unsigned short U16;
typedef char I8;
typedef unsigned char UI8;
const int MOD = 1e9 + 7;

#define loop(i,s,e) for(long long i=s;i<e;i++)
#define range(i,s,e) for(long long i=s;i<=e;i++)

ULL powermod(ULL x, ULL y)
{
    ULL temp;
    if( y == 0)
       return 1;
    temp = powermod(x, y/2);
    if (y%2 == 0)
        return (temp*temp)%MOD;
    else
    {
        if(y > 0)
            return (x*((temp*temp)%MOD))%MOD;
        else
            return (temp*temp)/x;
    }
}

using namespace std;
/***********************************************************************************/

int N;
int result;
map < int, bool> dig;

void process(int n){
 //   cerr<<n<<" :";
    while(n){
        dig[n%10] =true;
  //      cerr<<n<<" ";
        n = n/10;
    }//cerr<<endl;
}

void go(){
    result = 0;
//    cerr<<"solving.."<<endl;
    if(N){

        dig.clear();
        int i = 1;
//        cerr<<N<<"#"<<endl;
        while(dig.size()!=10){
            process(i*N); i++;
        }
        result = (i-1) * N;
    }
}
class Solution
{
public:
int T;
    Solution(){ T=1; }
    void solve();
    void input(){
        cin>>T;
        loop(t,1,T+1){
            cin>>N;
 //           cerr<<"ssdf"<<endl;
            go();
            cout<<"Case #"<<t<<": ";
            if(result) cout<<result<<endl;
            else cout<<"INSOMNIA"<<endl;
        }
    }
    void output(){
    }
};

void Solution::solve(){

}

int main()
{
#ifdef LOCAL_BUILD
    freopen("input.txt","r",stdin);
    freopen("debug.txt","w",stderr);
    freopen("output.txt","w",stdout);
#endif
    Solution S;
    S.input();
    S.output();
    return 0;
}
