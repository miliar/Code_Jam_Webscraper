#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdlib>
#include <list>
#include <set>
#include <ctime>
#include <list>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define vi vector<int>
#define vd vector<double>
#define pii pair<int,int>
#define pdd pair<double,double>
#define ll long long
#define INF (1<<30)
using namespace std;

int C, D, V;
vector<int> A;
const int maxV = 110;

int fnd() {
    int i, j;
    bool poss[maxV];
    poss[0] = true;
    for(i = 1; i <= V; ++i) {
        poss[i] = false;
    }
    for(i = 0; i < A.size(); ++i) {
        for(j = V; j >= A[i]; --j) {
            if(poss[j - A[i]]) {
                poss[j] = true;
            }
        }
    }
    for(i = 1; i <= V; ++i) {
        if(!poss[i]) return i;
    }
    return -1;
}

void small() {
    int i, j, ans = 0;
    cin >> C >> D >> V;
    A.resize(D);
    for(i = 0; i < D; ++i) cin >> A[i];
    while(1) {
        j = fnd();
        if(j == -1) break;
        ++ans;
        A.pb(j);
        sort(A.begin(), A.end());
    }
    cout << ans << '\n';
}

void solve_case(int case_id)
{
    printf("Case #%d: ", case_id);
    small();
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
