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

int N, X;
vector<int> A;

int sc(vector<int> v)
{
    if(v.size() == 1) return -1;
    int i = (int) v.size() - 1, j;
    vector<int>::iterator it = lower_bound(v.begin(), v.end() - 2, X - v[i]);
    j = it - v.begin();
    if(v[i] + v[j] <= X) return j;
    return j - 1;
}

void solve_case(int case_id)
{
    printf("Case #%d: ", case_id);
    int i, j, ans = 0;
    cin >> N >> X;
    A.clear();
    A.resize(N);
    for(i = 0; i < N; ++i) cin >> A[i];
    sort(A.begin(), A.end());
    while(A.size() > 0)
    {
        j = sc(A);
        A.pop_back();
        if(j != -1) A.erase(A.begin() + j);
        ++ans;
    }
    cout << ans << '\n';
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
