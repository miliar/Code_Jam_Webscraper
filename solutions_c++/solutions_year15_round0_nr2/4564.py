#include <bits/stdc++.h>
using namespace std;

int mn, maxtop;
void brute(int, priority_queue<int>);
int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, z;
    cin >> t;
    for (z = 1; z <= t; z++){
        int n, x, i;
        mn = INT_MAX;
        priority_queue<int> pq;
        cin >> n;
        for (i = 0; i < n; i++) {
            cin >> x;
            pq.push(x);
        }
        maxtop = pq.top();
        brute(0, pq);
        cout << "Case #" << z << ": ";
        cout << mn << endl;
    }
    return 0;
}

void brute(int time, priority_queue<int> pq)
{
    if(time == maxtop + 1) return;

    mn = min(mn, time+pq.top());
    if (pq.top() != 1) {
        int x = pq.top();
        pq.pop();
        for (int i = 1; i <= x/2; i++) {
            priority_queue<int> temp;
            temp = pq;
            temp.push(i);
            temp.push(x-i);
            brute(time+1, temp);
        }
    }
}
