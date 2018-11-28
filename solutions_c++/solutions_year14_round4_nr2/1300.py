#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define fr(i,a,b) for(int i = (a); i < (b); ++i)
#define rep(i,n) fr(i,0,n)
#define cl(a,b) memset((a), (b), sizeof(a))
#define all(c) (c).begin(), (c).end()
#define _ << ", " <<
#define db(x) cerr << #x " == " << x << endl

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long long ll;
const int inf = 0x3f3f3f3f;

int n, x;

int A[1010];

int count_up(vector<int> v) {
    int n = v.size();
    int inversions = 0;
    rep (i,n) rep(j,n-1) {
	    if(v[j+1] < v[j]) {
		    swap(v[j], v[j+1]);
		    ++inversions;
	    }
    }
    return inversions;
}

int count_down(vector<int> v) {
    int n = v.size();
    int inversions = 0;
    rep (i,n) rep(j,n-1) {
	    if(v[j+1] > v[j]) {
		    swap(v[j], v[j+1]);
		    ++inversions;
	    }
    }
    return inversions;
}

void pv(vector<int> v) {
    rep(i,v.size()) cout << v[i] << " ";
    cout << endl;
}

int main() {
    int t;
    scanf("%d", &t);
    
    rep(tc, t) {
        printf("Case #%d: ", tc+1);
        
        scanf("%d", &n);
        
        rep(i,n) scanf("%d", &A[i]);
        
        int pos = max_element(A,A+n) - A;
        
        
        int rsp = inf;
        
        rep(i,n) {
            vi left, right;
            rep(j,n) {
                if (j == pos) continue;
                if (j == i) {
                    if (i < pos) right.push_back(A[j]);
                    else if (i > pos) left.push_back(A[j]);
                }
                if (j < i) left.push_back(A[j]);
                if (j > i) right.push_back(A[j]);
            }
            int ans = abs(pos - i);
            ans += count_up(left);
            ans += count_down(right);
            rsp = min(rsp, ans);
        }
        
        
       printf("%d\n", rsp);
    }

    return 0;
}
