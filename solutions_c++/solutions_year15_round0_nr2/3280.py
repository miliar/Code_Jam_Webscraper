#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <ctime>
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define ms0(x) memset((x),0,sizeof(x))
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define rep(i,m,n) for(int i=(m),_end=(n);i < _end;++i)
#define repe(i,m,n) for(int i=(m), _end =(n);i <= _end;++i)
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;
using namespace std;

bool solve(vector<int> st, int t) {
    for (int i = 0; i < t; i++) {
        int use = t - i;
        int cnt = i;
        for ( int j = st.size() - 1; j >= 0; j--) {
            if ((st[j]%use)==0) cnt -= st[j] / use - 1;
            else cnt -= st[j] / use;
        }
        if (cnt >= 0) return true;
    }
    return false;
}

int main(){
    freopen("./B-small-attempt1.in", "r", stdin);
    freopen("./b_small_result.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int num;
        cin >> num;
        vector<int> st;
        for (int i = 0; i < num; i++) {
            int tmp;
            cin >> tmp;
            st.push_back(tmp);
        }
        sort(st.begin(), st.end());
        int start = 0, end = st[st.size()-1];
        while (start < end - 1) {
            int mid = start + (end - start) / 2;
            if (solve(st, mid)) {
                end = mid;
            } else {
                start = mid;
            }
        }
        int res;
        if (solve(st,start)) res = start;
        else res = end;
        cout << "Case #" << (t + 1) << ": " << res << endl;
    }
	return 0;
}
