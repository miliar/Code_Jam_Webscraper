#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
vector <int> ans;
struct node 
{
    int id, val;
    node() {  }
    node(int _id, int _val) : id(_id), val(_val) {  }
    bool operator < (const node& rhs) const
    {
        return val < rhs.val;
    }
};
priority_queue <node> pq;
int main()
{
    int T, cas = 0;
    cin >> T;
    while (T--)
    {
        int n;
        cin >> n;
        while (!pq.empty()) pq.pop();
        ans.clear();
        for (int i = 0; i < n; ++i) 
        {
            int x;
            cin >> x;
            pq.push(node(i, x));
        }
        while (!pq.empty())
        {
            node u = pq.top();
            pq.pop();
            ans.push_back(u.id);
            if (u.val > 1) pq.push(node(u.id, u.val - 1));
        }
        printf("Case #%d:", ++cas);
        int cnt = (int) ans.size();
        if (cnt & 1)
        {
            for (int i = 0; i <= cnt - 4; i += 2) cout << " " << (char) ('A' + ans[i]) << (char) ('A' + ans[i + 1]);
            cout << " " << (char) ('A' + ans[cnt - 3]);
        }
        else 
        {
            for (int i = 0; i <= cnt - 3; i += 2) cout << " " << (char) ('A' + ans[i]) << (char) ('A' + ans[i + 1]);
        }
        cout << " " << (char) ('A' + ans[cnt - 2]) << (char) ('A' + ans[cnt - 1]) << endl;
     }
    return 0;
}
