#include <iostream>
#include <queue>
using namespace std;
void solve(priority_queue<int, vector<int>, less<int> >pq, int cur, int &ans) {
    if (!pq.empty()) {
        ans = min(cur + pq.top(), ans);
            
        int f = pq.top(); 
        pq.pop();
        if (f > 3) {
            for (int i = 2; i <= f / 2; i++) {
                auto newpq = pq;
                newpq.push(i);
                newpq.push(f - i);
                solve(newpq, cur + 1, ans);
            }
        }
        else
            return;
    }
}
int main() {
    int ncase;
    cin >> ncase;
    for (int i = 0; i < ncase; i++) {
        priority_queue<int, vector<int>, less<int> > pq;
        int n;
        cin>>n;
        for (int j = 0; j < n; j++) {
            int tmp;
            cin >> tmp;
            pq.push(tmp);
        }
        int ans = 1<<30;
        solve(pq, 0, ans);
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
