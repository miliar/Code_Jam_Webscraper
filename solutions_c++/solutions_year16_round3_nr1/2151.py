#include <bits/stdc++.h>

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> Pair;
typedef complex<double> Complex;

const double PI = M_PI;
const int INF = 1e9;

int main() {
    int N, T, k;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int sum = 0;
        cin >> N;
        //        vector<pair<int,int>> p;
        priority_queue<Pair> que;
        for(int i = 0; i < N; i++) {
            cin >> k;
            sum += k;
            if(k)
                que.push(make_pair(k, i));
        } 

        printf("Case #%d:", t);

        while(!que.empty()) {
            Pair a = que.top();
            que.pop();
            if(sum == 3) {
                sum--;
                a.first--;
                if(a.first) que.push(a);
                cout << " " << (char)(a.second+'A');
            } else {
                sum -= 2;
                Pair b = que.top();
                que.pop();
                a.first--;
                if(a.first) que.push(a);
                b.first--;
                if(b.first) que.push(b);
                cout << " " << (char)(a.second+'A') << (char)(b.second+'A');
            }
        }
        cout << endl;
    }
}


