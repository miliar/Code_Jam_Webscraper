#include <iostream>
using namespace std;
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <set>
#include <ctime>
#include <stack>
#include <list>
#include <cassert>
#include <iomanip>
#include <deque>
#include <sstream>
#include <fstream>
typedef pair<int,int> pii;
#define rep(i,j,n) for(i=j;i<n;i++)
#define pb push_back
#define ff first
#define ss second 
#define lli long long int
#define get getchar

inline int scan() {
    int n=0,s=1;
    char p=get();
    if(p=='-')  s=-1;
    while((p<'0'||p>'9')&&p!=EOF&&p!='-') p=get();
    if(p=='-') s=-1,p=get();
    while(p>='0'&&p<='9') { n = (n<< 3) + (n<< 1) + (p - '0'); p=get(); }
    return n*s;
}
string ans;
void func(int r, int p, int s, string tmp, queue<char> xx) {
    if (r+p+s == 0) {
        bool f = 1;
        //cout << tmp << " "  << xx.size() << " ";
        while(xx.size() != 1) {
            char a1 = xx.front();
            xx.pop();
            char a2 = xx.front();
            xx.pop();
            //cout << a1 << " " << a2 << " ";
            if (a1 == a2) {
                f = 0;
                break;
            }
            if (a1 > a2) swap(a1,a2);
            if (a1 == 'P' and a2 == 'R') {
                xx.push('P');
            }
            if (a1 == 'P' and a2 == 'S') {
                xx.push('S');
            }
            if (a1 == 'R' and a2 == 'S') {
                xx.push('R');
            }
        }
        //cout << endl;
        if (f) {
            if (ans.size() == 0)
                ans = tmp;
            if (ans > tmp) ans = tmp;
        }
    }
    if (r) {
        queue<char> gg = xx;
        gg.push('R');
        string tmp1 = tmp;
        tmp1.push_back('R');
        func(r-1,p,s,tmp1,gg);
    }
    if (p) {
        queue<char> gg = xx;
        gg.push('P');
        string tmp1 = tmp;
        tmp1.push_back('P');
        func(r,p-1,s,tmp1,gg);
    }
    if (s) {
        queue<char> gg = xx;
        gg.push('S');
        string tmp1 = tmp;
        tmp1.push_back('S');
        func(r,p,s-1,tmp1,gg);
    }
}
int main() {
        
    ios::sync_with_stdio(false);
    
    //clock_t start = std::clock();
    freopen ("inp.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    //cout << "Time: " << (std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000) << " ms" << std::endl;

    int t; cin >> t;
    string nnn = "IMPOSSIBLE";
    for (int ca = 1; ca <= t; ca++) {

        cout << "Case #" << ca << ": ";
        int n,r,p,s;
        cin >> n >> r >> p >> s;

        int x = (1<<n);

        if (2*r > x or 2*p > x or 2*s > x) {
            cout << nnn << endl;
            continue;
        }
        ans = "";
        string tt = "";
        queue<char> ee;
        func(r,p,s,tt,ee);
        if (ans.size() == 0) {
            ans = nnn;
        }
        cout << ans << endl;
    }
    
    
    return 0;
        
}