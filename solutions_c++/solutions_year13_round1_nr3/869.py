#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;

#define rep(i,a) for((i)=0;(int)(i)<(a);(i)++)
#define rrep(i,a,b) for((i)=(a);(i)>=(b);(i)--)
#define maX(a,b) ((a)>(b)?(a):(b))
#define miN(a,b) ((a)<(b)?(a):(b))
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pis pair<int,string>
#define psi pair<string,int>
#define pss pair<string,string>
#define ll long long
#define ull unsigned long long
#define fi first
#define se second
#define re return
#define sz(x) ((int)(x).size())
#define vi vector<int>
#define vs vector<string>
#define vpii vector< pii >

template<class T> T abs(T x){return x>0?x:-x;}
inline int toInt(string s) {int v;istringstream sin(s);sin>>v;return v;}
inline ll toll(string s) {ll v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> inline T sqr(T x) {return x*x;}
template<class T> inline T gcd(T a,T b) {if (a<0) a=-a;if (b<0) b=-b;return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b) {return a*(b/gcd(a,b));}

int main()
{

    int test,R,N,M,K,Test,mask,i,a1,a2,a3;
    cin>>Test;
    for(test=1;test<=Test;test++){
        printf("Case #%d:\n",test);
        cin>>R>>N>>M>>K;
        vi P(K);
        
        for(int r=0;r<R;r++){
			bool f=0;
            rep(i,K)cin>>P[i];
            for(a1=2;a1<=M;a1++){
                for(a2=2;a2<=M;a2++){
                    for(a3=2;a3<=M;a3++){
                        int t=0;
                        vi p=P;
                        for(mask=0;mask<(1u<<N);mask++){
                            int prod=1;
                            if(mask&(1u<<0))prod*=a1;
                            if(mask&(1u<<1))prod*=a2;
                            if(mask&(1u<<2))prod*=a3;
                            for(i=0;i<K;i++){
								if(prod==p[i]){t++;p[i]=-1;}
							}
                        }
                        if(t>=K-1){
                            cout<<a1<<a2<<a3;
                            f=1;
                            break;
                        }
                    }
                    if(f)break;
                }
                if(f)break;
            }
           
            if(!f)cout<<111;
            cout<<endl;
            
        }
       

    }
}

