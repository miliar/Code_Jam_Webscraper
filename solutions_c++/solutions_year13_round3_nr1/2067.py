#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<cmath>
#include<algorithm>
#include<climits>
#include<set>
#include<deque>
#include<queue>
#include<map>
#include<climits>
#include<string>
#include<stack>
#include<sstream>
using namespace std;
#define pi (2.0*acos(0.0))
#define eps 1e-6
#define ll long long
#define inf (1<<30)
#define vi vector<int>
#define vll vector<ll>
#define sc(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
#define all(v) v.begin() , v.end()
#define me(a,val) memset( a , val ,sizeof(a) )
#define pb(x) push_back(x)
#define pii pair<int,int> 
#define mp(a,b) make_pair(a,b)
#define Q(x) (x) * (x)
#define L(x) ((x<<1) + 1)
#define R(x) ((x<<1) + 2)
#define M(x,y) ((x+y)>>1)
#define fi first
#define se second
#define MOD 10009
#define N 1005

string vocales = "aeiou";

bool con(char x){
    for(int i = 0 ; i < vocales.size() ; i++)
        if( vocales[i] == x ) return 0;
    return 1;
}


int main(){
    int tc , n;
    cin >> tc;
    string s;
    for(int test = 1 ; test <= tc ; test++){
        printf("Case #%d: ",test);
        cin >> s >> n;
        //cout << s << " " << n << endl;
        int ans = 0;
        for(int i = 0 ; i < s.size() ; i++){
            int ct = 0;
            for(int j = i ; j < s.size() ; j++){
                if( con( s[j] ) ) ct++;
                else ct = 0;
                if( ct >= n ){
                    ans += s.size() - j;
                    ct = 0;
                    break;
                }
            }
            if( ct >= n ) ans++;
        }
        cout << ans << endl;
    }
    return 0;
}
