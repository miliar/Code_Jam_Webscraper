#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <algorithm> // max...
#include <utility> // pair
#include <complex>
#include <climits> // int, ll...
#include <limits> // double...
#include <cmath> // abs, atan...
#include <cstring> // memset
#include <string>
#include <functional> // greater, less...
#include <bitset>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, double> id;
typedef pair<double, int> di;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> dd;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef vector<dd> vdd;
typedef vector<id> vid;
typedef vector<vi> vvi;
typedef map<int, int> mii;
typedef map<int, ll> mil;
typedef map<ll, ll> mll;

#define ONLINE_JUDGE

int main() {
    #ifdef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        freopen("A-large.out", "w", stdout);
        //freopen("X-large-practice.in", "r", stdin);
        //freopen("X-large-practice.out", "w", stdout);
    #endif

    #ifndef ONLINE_JUDGE
        freopen("input.in", "r", stdin);
        //freopen("output.out", "w", stdout);
    #endif

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        printf("Case #%d:", t);
        int N; cin >> N;
        priority_queue<pair<int, char>> pq;
        char c = 'A';
        while (N--) {
            int p; cin >> p;
            pq.push(make_pair(p, c));
            c++;
        }

        int a1 = pq.top().first;
        char p1 = pq.top().second;
        pq.pop();

        bool second = false;
        int a2; char p2;
        if (!pq.empty()) {
            second = true;
            a2 = pq.top().first;
            p2 = pq.top().second;
            pq.pop();

            while (a1 > a2) {
                cout << ' ' << p1;
                a1--;
            }
        }

        while (!pq.empty()) {
            int a = pq.top().first;
            char p = pq.top().second;
            pq.pop();
            cout << ' ' << p;
            if (a != 1) pq.push(make_pair(a-1, p));
        }

        while (a1 != 0) {
            cout << ' ' << p1; a1--;
            if (second) cout << p2;
        }

        cout << endl;
    }

    return 0;
}