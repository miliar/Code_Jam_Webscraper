#include <bits/stdc++.h>
using namespace std;
int ma, mtop;
void brute(int,
priority_queue<int>);
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, z;
    cin >> t;
    for (z = 1; z <= t; z++){
        int n, x, i; ma = INT_MAX;
  	     priority_queue<int> pq; cin >> n;
  	     for (i = 0; i < n; i++)
       	 {
  	        cin >> x; pq.push(x);
  	     }
  	     mtop = pq.top();
  	     brute(0, pq);
        cout << "Case #" << z << ": ";
        cout << ma << endl;
    }
    return 0;
}

void brute(int time, priority_queue<int> pq) {
    if(time == mtop + 1)
        return;
    ma = min(ma, time+pq.top());
    if (pq.top() != 1) {
        int x = pq.top(); pq.pop();
        for (int i = 1; i <= x/2; i++)
        {
            priority_queue<int> temp;
            temp = pq; temp.push(i);
            temp.push(x-i);
            brute(time+1, temp);
        }
    }
}
