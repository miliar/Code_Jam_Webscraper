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
bool verify(int id, vector<string> s, int n, string cur, int ord[]) {
    if (id == n) {
        return 1;
    }

    int okay = 0;
    int gg = ord[id];
    for (int i = 0; i < n; i++) {
        if (cur[i] == '0' and s[gg][i] == '1') {
            cur[i] = '1';
            if (!verify(id+1,s,n,cur,ord)) {
                return 0;
            }
            cur[i] = '0';
            okay++;
        }
    }

    if (okay == 0) return 0;
    return 1;
}

int main() {
        
    ios::sync_with_stdio(false);
    
    //clock_t start = std::clock();
    freopen ("inp.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    //cout << "Time: " << (std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000) << " ms" << std::endl;

    int t; cin >> t;
    int biti = 0;
    for (int ca = 1; ca <= t; ca++) {
        cout << "Case #" << ca << ": ";
        int n;
        cin >> n;
        vector <string> s(n);
        for (int i = 0; i < n; i++)
            cin >> s[i];
        int minc = n*n;
        string ini = "";
        for (int i = 0; i < n; i++)
            ini.push_back('0');
        for (int i = 0; i < (1<<(n*n)); i++) {
            int cost = __builtin_popcount(i);
            vector <string> tmp(n);
            for (int r = 0; r < n; r++) {
                tmp[r] = s[r];
                for (int c = 0; c < n; c++) {
                    if (i&(1<<(r*n+c)))
                        tmp[r][c] = '1';
                }
            }
            int ord[n];
            for (int i = 0; i < n; i++)
                ord[i] = i;
            bool f = 1;
            do {
                if (!verify(0,tmp,n,ini,ord)) {
                    f = 0;
                    break;
                }
            } while (next_permutation(ord,ord+n));
            if (f)
                if (minc > cost) minc = cost,biti = i;
        }
        cout << minc << endl;
    }
    
    
    return 0;
        
}