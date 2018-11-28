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
using namespace std;
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

bool isPrime(ULL number, ULL &div)
{
    ULL i;
    for (i=2; i<number; i++)
    {
        if(number% i==0){
            div = i;
            return false;
        }
    }
    return true;
}


/***********************************************************************************/
int N,J;
map<ULL,bool> primes;
map<ULL,ULL> divs;
ULL primenum[1000000];
int pCnt;


class Solution
{
public:
int T;
    Solution(){ T=1; }
    void solve();
    void input(){
        ULL tt,d;

        for(ULL n=2;n<=(pow(10,5)); n++){
            bool p = isPrime(n, d);
            if(p) {
                primenum[pCnt++] = n;
                primes[n] = true;
                //cerr<<n<<" ";
            }
        }
        //cerr<<pCnt<<endl;
        cin>>T;
        loop(t,1,T+1){
            cin>>N>>J;
            cout<<"Case #"<<t<<":"<<endl;
            solve();
        }
    }
    void output(){
    }
};
ULL num_in_base(int n, int base){
    ULL num = 0;
    int bit,i;
    i = 0;
    while(n){
        bit = n & 1;
        if(bit){
            num += bit*pow(base,i);
        }
        i++;
        n >>= 1;
    }
    return num;
}

ULL mulMod(ULL num, int m, int mod){
    ULL ans = 1;
    if(m==0) return 1;
    cerr<<"$ "<<m<<" "<<num<<" "<<mod<<" ";
    for(int i=0;i<m;i++){
        ans = (ans*(num%mod))%mod;
    }
    cerr<<ans<<endl;
    return ans;
}
bool isDivisible(ULL num, int base, int pnum){
    ULL sum=0;
    int bit,i=0;
//    cerr<<num<<" "<<base<<" "<<pnum<<" #";
    while(num){
        bit = num&1;
        if(bit){
            sum =  (sum + mulMod(base,i,pnum)) % pnum;
        }
        i++;
        num >>= 1;
    }
//    cerr<<sum<<endl;
    return sum%pnum == 0;
}
void Solution::solve(){
    int j = 0;
    for(ULL n=(1<<(N-1))+1; n<(1<<N) ; n+=2){
 //       cerr<<n<<" ";
        ULL num;
        ULL divisor[11];
        ULL div;
        int base;
        bool isP;
        for(base = 2 ; base <=10 && !isP; base++){
            isP = false;
            int i;
            for(i=0;i<pCnt;i++){
                if(isDivisible(n,base,primenum[i])){
                    if(N<=17 && num_in_base(n,base) == primenum[i]) continue;
//                    cerr<<n<<" is divisible in "<<base<<" by "<<primenum[i]<<endl;
                    divisor[base] = primenum[i];
                    break;
                }
            }
            if(i==pCnt) break;
           /* num = num_in_base(n, base);
            divisor[base] = 0;
            cerr<<num<<" ";
            if(!isPrime(num, div)){
                divisor[base] = div;
            }else
                break;*/
        }//cerr<<endl;
        if(base == 11){
            loop(i,0,N){
                cout<<((n>>(N-i-1)) & 1);
            }
            loop(b,2,11){
                cout<<" "<<divisor[b];
            }
            cout<<endl;
            j++;
            if(j==J) return;
        }
    }
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
