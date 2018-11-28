#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <ctype.h>
#include <stack>
#include <queue>
#include <limits.h>
#include <fstream>
#include <map>
#include <set>

#define rep(i, a) for(long long int i = 0; i < a; i++)
#define rep1(i, a) for(long long int i = 1; i <= a; i++)
#define fo(i, a, b) for(long long int i = a; i < b; i++)
#define defo(i, a, b) for(long long int i = a; i >= b; i--)
#define ll long long
#define Int long long int
#define pr(i) printf("Case #%lld: ",i)
#define pb push_back
#define sz(a) ((long long int)(a.size()))
#define x first
#define y second
#define fin(e) freopen("e.txt","r",stdin)
#define fout(e) freopen("e.txt","w",stdout)
#define mp make_pair
#define SET(x, a) memset(x, a, sizeof(x));
#define pi  3.1415926535897
#define mod 1000000007
#define retunr return
using namespace std;

typedef vector<long long int> vi;
typedef vector<ll> vll;
typedef pair<long long int, long long int> pii;
typedef pair<ll, ll> pll;
int main(){
    freopen("inpp.in","r",stdin);
    freopen("output.txt","w",stdout);
    Int test,l=0;
    cin>>test;
    while(test--){
        l++;
        Int n;
        scanf("%lld",&n);
        string str;
        cin>>str;
        Int i;
        Int ans = 0;
        Int total = 0;
        total+=str[0]-'0';
        for(i=1;i<str.size();i++){
            Int req = i;
            ans = ans+max(req-total,0LL);
            total = max(total,req);
            total+=str[i]-'0';
        }
        pr(l);
        cout<<ans<<"\n";
    }
    return 0;
}
