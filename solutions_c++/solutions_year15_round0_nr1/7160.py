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
#include <fstream>
using namespace std;

#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define SZ(c) (ll)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define ll long long
#define ld long double
#define pii pair< ll, ll >
#define psi pair< string, ll >
int main(){
    int t;
    ifstream in("input1.in");
    ofstream out("output.out");
    in>>t;
    for(int j=1;j<=t;j++){
        int n;
        in>>n;
        string s;
        in>>s;
        int tem=0,ans=0;
        for(int i=0;i<=n;i++){
            if(tem>=i){
                tem+=s[i]-'0';
            }
            else{
                ans += i-tem;
                tem += (i-tem)+s[i]-'0';
            }
        }
        out<<"Case #"<<j<<": "<<ans<<endl;
    }
    out.close();
}

