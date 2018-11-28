//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

//defines-general
#define to(a) __typeof(a)
#define all(vec)  vec.begin(),vec.end()
#define fill(a,val)  memset(a,val,sizeof(a))

//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)



//defines-pair
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

// my own
#define sl(a) scanf("%lld",&a)
#define sll(a,b) scanf("%lld%lld",&a,&b)
#define slll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define sllll(a,b,c,d) scanf("%lld%lld%lld%lld",&a,&b,&c,&d)


int main(){
    int t;
    cin >> t;
    for(int tt = 1;tt <= t; tt++){
        printf("Case #%d: ", tt);
        ll n;
        cin >> n;
        ll inc = n;
        bool digs[10];
        repi(i, 0, 10){
            digs[i] = 0;
        }
        bool nahua;
        if(n==0) {
            cout <<"INSOMNIA"<<endl;
            continue;
        } else {
            do{
                ll nc = n;
                while(nc>0){
                    digs[nc%10] = 1;
                    nc/=10;
                }
                nahua = false;
                repi(i,0,10) if(!digs[i]) nahua = true;
                n += inc;
            }while(nahua);
        }
        cout<<n-inc<<endl;
    }
}
