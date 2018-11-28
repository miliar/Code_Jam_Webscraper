//#include<bits/stdc++.h>
#include<iostream>
#include<math.h>
#include<set>
#include<vector>
#include<queue>

#define ii pair<int, int>
#define PB push_back

using namespace std;

int eat[1000 + 10], divide[1000 + 10], best, D, cases;
ii bestDivide[1000 + 10];
vector<int> pan;

void print() {
    cout << "Vector: ";
    for(int i = 0; i < pan.size(); i++) cout << pan[i] << " ";
    cout << endl;
}

void solve(priority_queue<int> q, int a, int b, int op) {
        if(op > best) return;
        q.push(a); q.push(b);
        op++;
        int n = q.top(); q.pop();
        best = min(best, op + n);
        if(n <= 3) return;
        for(int j = 1; j <= (n + 1) / 2; j++)
            solve(q, n - j, j, op);
}


inline int get(int x, int j) {
    return (divide[x - j] + divide[j] + 1);
}

/*void precalc() {
    eat[1] = 1; eat[2] = 2; eat[3] = 3;
    divide[1] = divide[2] = divide[3] = 0;

    for(int i = 4; i <= 1000; i++) {
        int mini = INT_MAX;
        divide[i] = INT_MAX;
        for(int j = 1; j <= (i + 1) / 2; j++)
            if(get(i, j) < divide[i]) divide[i] = get(i, j);

        for(int j = 1; j <= (i + 1) / 2; j++){
            int aux = max(eat[i - j], eat[j]);
            if(get(i, j) == divide[i] && aux < mini) {
                mini = aux;
                bestDivide[i] = ii(i - j, j);
            }
        }
        eat[i] = mini;
        /*cout <<"->" <<  i << endl;
        cout << divide[i] << endl;
        cout << eat[i] << endl;
        cout << bestDivide[i].first << "-" << bestDivide[i].second << endl;
        system("pause");
    }
}*/


int nTest;
int main() {
    freopen("Inputs.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //precalc();
    cin >> nTest;
    while(nTest--) {
        pan.clear();
        cin >> D;
        priority_queue<int> q;
        best = -1;
        for(int i = 0; i < D; i++) {
            int aux;
            cin >> aux;
            q.push(aux);
            best = max(best, aux);
        }
        solve(q, 0, 0, -1);
        printf("Case #%d: %d\n",++cases, best);
    }



}
