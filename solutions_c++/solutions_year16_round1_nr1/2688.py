#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
#include <functional>
using namespace std;

#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define ll long long
#define ld long double
#define mod 1000000007
#define inf 1061109567LL
#define pii pair< int, int >
#define pll pair< ll, ll >
#define psi pair< string, int >
int main(int argc, char const *argv[])
{
    int t;
    cin>>t;
    int T=1;
    while(t--){
        string s;
        cin>>s;
        int n = s.size();
        char ans[3*n];
        int l=n,r = n;
        ans[r] = s[0];
        r++;
        l--;
        for(int i=1;i<n;i++){
            if(s[i]>=ans[l+1]){
                ans[l]=s[i];
                l--;
            }
            else{
                ans[r]=s[i];
                r++;
            }
        }
        cout<<"Case #"<<T<<": ";
        for(int i=l+1;i<r;i++){
            cout<<ans[i];
        }
        T++;
        cout<<endl;
    }
    return 0;
}