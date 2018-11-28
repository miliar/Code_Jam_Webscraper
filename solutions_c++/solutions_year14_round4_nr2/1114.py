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

int N;
int A[1024], U[1024];

int get_ind(int el)
{
    for(int i = 0; i < N; ++i)
    {
        if(A[i] == el) return i;
    }
}

void solve_case(int case_id)
{
    printf("Case #%d: ", case_id);
    int i, j, v, k, l, mask, cr, best = INF;
    cin >> N;
    for(i = 0; i < N; ++i) cin >> A[i];
    vector<int> B, C;
    for(i = 0; i < N; ++i) U[i] = A[i];
    for(mask = 0; mask < (1<<N); ++mask)
    {
        B.clear(); C.clear();
        for(i = 0; i < N; ++i)
        {
            if(mask & (1<<i)) B.pb(A[i]);
            else C.pb(A[i]);
        }
        sort(B.begin(), B.end());
        sort(C.begin(), C.end());
        cr = 0;
        for(i = 0; i < B.size(); ++i)
        {
            k = get_ind(B[i]);
            if(k == i) continue;
            cr += k - i;
            v = A[k];
            for(j = k; j > i; --j) A[j] = A[j - 1];
            A[i] = v;
        }
        for(i = 0; i < C.size(); ++i)
        {
            l = N - i - 1;
            k = get_ind(C[i]);
            if(k == l) continue;
            cr += l - k;
            v = A[k];
            for(j = k; j < l; ++j)
            {
                A[j] = A[j + 1];
            }
            A[l] = v;
        }
        best = min(best, cr);
        for(i = 0; i < N; ++i) A[i] = U[i];
    }
    cout << best << '\n';
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
