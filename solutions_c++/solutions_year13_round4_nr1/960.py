#include <cstdio>
#include <iostream>
#include <stack>
using namespace std;

long long sta_lst[1000], total;
int N, M;
stack<int> stk;
long long cost(int a, int b) {
    int r = b - a;
    return (r * (2*N - r + 1 )) /2;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.output", "w", stdout);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {

        cin >> N >> M;
        for (int i=0; i<1000; i++) {
            sta_lst[i] = 0;
        }
        total = 0;
        while (!stk.empty()) {
            stk.pop();
        }
        for (int i=0; i<M; i++) {
            int x, y, p;
            cin >> x >> y >> p;
            total += cost(x, y) * p;
            sta_lst[x] += p;
            sta_lst[y] -= p;
        }
        for (int i=1; i<=N; i++) {
            while (sta_lst[i] > 0) {
                stk.push(i);
                sta_lst[i]--;
            }
            while (sta_lst[i] < 0) {
                total -= cost(stk.top(), i);
                stk.pop();
                sta_lst[i]++;
            }
        }
        
        cout << "Case #" << test << ": " << total % 1000002013 << endl;
    }
    
    return 0;
}