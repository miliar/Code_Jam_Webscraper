#include <cstdlib>
#include <climits>
#include <cstdio>
#include <cstring>
#include <cmath>

// STL
#include <sstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map> // contains multimap
#include <set> // contains multiset
#include <queue> // contains priority_queue
#include <deque>
#include <list>
#include <stack>

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

using namespace std;

typedef unsigned long long ul;
typedef long long ll;

#define SIZE 10000

int N, X;
int input[SIZE];
list<int> disc;

int solve() {
    sort(input, input+N, greater<int>());
    list<int> l (input, input + N);
    
    int c = 0;
    while (!l.empty()) {
        c += 1;
        int cap = l.front();
        l.pop_front();
    
        if (l.empty()) break;

        if (l.back() + cap <= X)
            l.pop_back();
    }

    return c;
}


int main() {
    int numcase;

    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> numcase;
    for (int i = 0; i < numcase; ++i) {
        cin >> N >> X;
        memset(input, 0, sizeof(int)*N);
        for  (int j = 0; j < N; ++j) {
            cin >> input[j];
        }
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }

    return 0;
}
