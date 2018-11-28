/* Author => Aakash Prakash (akki744) */
#include<bits/stdc++.h>

#define MOD 1000000007
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define SET(a,val) memset(a, val, sizeof(a))

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define SC(x) scanf("%d",&x)
#define SCL(x) scanf("%lld",&x)
#define SCC(x) scanf("%c",&x)
#define SCS(x) scanf("%s",x)
#define SCU(x) scanf("%llu",&x)

#define PF printf

#define PB(x) push_back(x)
#define MP(a,b) make_pair(a,b)

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

typedef  pair<int,int> 	         pii;
typedef  vector<int> 	         vi;

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

LL gcd(LL a, LL b){
    if(b==0)
	return a;
    return gcd(b,a%b);
}

LL lcm(LL a, LL b){
    return (a*b)/gcd(a,b);
}

int len,arr[18];

bool isTidy(LL n){
    if((n/10)==0){
        return true;
    }
    int curr,prev=n%10;
    n/=10;
    while(n){
        curr=n%10;
        n/=10;
        if(curr>prev){
            return false;
        }
        prev=curr;
    }
    return true;
}

int calculate(LL n, int i){
    if(n==0){
        return 0;
    }
    arr[i]=n%10;
    return 1+calculate(n/10, i+1);
}

char str[1005];

int main() {
    int t;
    SC(t);
    REP(z,t){
        SCS(str);
        int k;
        SC(k);
        int moves=0;
        bool flag=true;
        int n=strlen(str);
        PF("Case #%d: ",(z+1));
        REP(i,n){
            if(str[i]=='+'){
                continue;
            }
            if(i>n-k){
                flag=false;
                break;
            }
            moves++;
            FOR(j,i,i+k-1){
                if(str[j]=='+'){
                    str[j]='-';
                }else{
                    str[j]='+';
                }
            }
        }
        if(!flag){
            PF("IMPOSSIBLE\n");
        }else{
            PF("%d\n",moves);
        }
    }
    return 0;
}

//time_t t=clock();
//cout<<(double)(clock()-t)/CLOCKS_PER_SEC<<endl;
