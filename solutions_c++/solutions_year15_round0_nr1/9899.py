#include <algorithm>
#include <bitset>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

#define inf 1<<30
#define eps 1e-8
#define pi acos(-1)
#define mod 1000000007

#define vi vector<int>
#define pb(x) push_back(x)
#define f(i,x,y) for(int i=x;i<y;i++)
#define rf(i,y,x) for(int i=y;i>=x;i--)
#define cerr1(x) cerr<<x<<endl
#define cerr2(x,y) cerr<<x<<" "<<y<<endl
#define bit(x) __builtin_popcount(x)
#define clr(a, val) memset(a, val, sizeof(a))
#define sorta(a) sort(a, 0, sizeof(a))
#define sortv(x) sort((x).begin(),(x).end())
string tos(int a) { ostringstream os(""); os << a; return os.str(); }

int T, X;
string s;

int main() {
    ios::sync_with_stdio(1); 
    
    #ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif  
    
    cin>>T;
    f(j, 1, T+1){
    
        cin>>X>>s;
        long long res = 0;
        long long cont=0;
        cont=s[0]-'0';
        f(i, 1,X+1){
            if(cont<i){
                res+= (i-cont);
                cont+=(s[i]-'0' + (i-cont));
            }
            else{
                cont+=(s[i]-'0');
            }
        }
        cout<<"Case #"<<j<<": "<<res<<"\n";
    }
}