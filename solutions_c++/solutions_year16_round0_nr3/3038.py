#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>

//using namespace __gnu_pbds;
using namespace std;

#pragma comment(linker, "/STACK:16777216")

#define Foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define rof(i,a,b) for(int (i)=(a);(i) > (b); --(i))
#define rep(i, c) for(auto &(i) : (c))
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define PB pop_back()
#define iOS ios_base::sync_with_stdio(false)
#define sqr(a) (((a) * (a)))
#define pow2(a) (((a) * (a)))
#define all(a) a.begin() , a.end()
#define error(x) cerr << #x << " = " << (x) <<endl
#define Error(a,b) cerr<<"( "<<#a<<" , "<<#b<<" ) = ( "<<(a)<<" , "<<(b)<<" )\n";
#define errop(a) cerr<<#a<<" = ( "<<((a).x)<<" , "<<((a).y)<<" )\n";
#define coud(a,b) cout<<fixed << setprecision((b)) << (a)
#define L(x) (((x)<<1)+1)
#define R(x) (((x)<<1)+2)
#define umap unordered_map
//#define double long double
// #define mod 1000000007
#define mod1 1000000009
#define LIMIT 10000000000000000LL
#define MAX1 1000000000
//#define si(n) scanf("%d",&n)
//#define sii(n,m) scanf("%d%d",&n,&m)
//#define pi(n) printf("%d\n",n)
const int inf=0x3f3f3f3f;
const long double pi=acos(-1.0);
#define INF 1000000000000000000LL
#define MAX 1000005
#define N 410
const string debug_line="yolo";
#define debug error(debug_line)
const double PI=4*atan(1);
#define read() freopen("mergedoutput.txt","r",stdin)
#define write() freopen("output.txt","w",stdout)
//template <typename T> using os =  tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
typedef long long ll;
typedef pair<int,int>pii;
typedef vector<int> vi;
typedef complex<double> point;

long long mulmod(long long a,long long b,long long c){
    long long x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}

int modulo(int a,int b,int c){
    long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x=(x*y)%c;
        }
        y = (y*y)%c; // squaring the base
        b /= 2;
    }
    return x%c;
}

bool Miller(long long p,int iteration){
    if(p<2){
        return false;
    }
    if(p!=2 && p%2==0){
        return false;
    }
    long long s=p-1;
    while(s%2==0){
        s/=2;
    }
    for(int i=0;i<iteration;i++){
        long long a=rand()%(p-1)+1,temp=s;
        long long mod=modulo(a,temp,p);
        while(temp!=p-1 && mod!=1 && mod!=p-1){
            mod=mulmod(mod,mod,p);
            temp *= 2;
        }
        if(mod!=p-1 && temp%2==0){
            return false;
        }
    }
    return true;
}

ll findDivisor(ll val1){
    // printf("trying %lld->",val1);
    for(ll j=2;j<=sqrt(val1);j++){
        if(val1%j==0){
            // printf("found %lld\n",j);
            return j;
        }
    }
    // printf("found 0\n");
    return 0;
}

int main(){
	ll val=(ll)(1<<15);
	val+=1;
	printf("%lld\n",val);
    int count1=0;

    For(i,val,val+200001){
        if(i%2==0){
            continue;
        }
        else{
            vi v1;
            For(j,0,16){
                if((1<<j) & i){
                    v1.pb(1);
                }
                else{
                    v1.pb(0);
                }
            }
            // printf("%d-->>\n",i);
            bool poss=true;
            For(j,2,11){
                ll val1=0;
                ll powv=1;
                For(k,0,16){
                    val1=val1+v1[k]*powv;
                    powv=powv*j;
                }
                if(findDivisor(val1)==0){
                    poss=false;
                    break;
                }
            }
            if(poss){
                count1++;
                if(count1>50){
                    break;
                }
                // printf("%d->",count1);
                reverse(all(v1));
                For(k,0,16){
                    printf("%d",v1[k]);
                }
                reverse(all(v1));
                printf(" ");
                For(j,2,11){
                    ll val1=0;
                    ll powv=1;
                    For(k,0,16){
                        val1=val1+v1[k]*powv;
                        powv=powv*j;
                    }
                    printf("%lld ",findDivisor(val1));
                }
                printf("\n");
            }
        }
    }

    printf("count is ->%d\n",count1);
}