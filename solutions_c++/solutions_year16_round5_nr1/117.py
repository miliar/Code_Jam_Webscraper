#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
using namespace std;

#define rep(i,n) for (int i=1;i<=(n);++i)
#define rep2(i,x,y) for (int i=(x);i<=(y);++i)
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VII;

string a;
vector<char> b;
int n;
int f[1000000][3];
const int inf =100000000;
stack<char> st;
void MAIN(){
    cin >> a;
    n = a.length();
    while (!st.empty()) st.pop();
    int ans=0;
    rep2(i,0,n-1)
        if (st.empty())
            st.push(a[i]);
        else if (st.top() == a[i]) {
            ans += 10;
            st.pop();
        } else {
            st.push(a[i]);
        }
    ans+=(5*(int)st.size())/2;
    cout << ans <<endl;
}

int main() {
    freopen("d:\\oi\\gcjr3\\A-large (1).in","r",stdin);
    freopen("d:\\oi\\gcjr3\\A-large (1).out","w",stdout);
    int tt;
    cin >> tt;
    rep(i,tt)
    {
        printf("Case #%d: ",i);
        MAIN();
    }    
    return 0;
}