#include <iostream>
#include <queue>
using namespace std;



int main() {
    int T, n;
    cin >> T;
    int cas = 1;
    while(T--) {
        cin >> n;
        priority_queue<pair<int,int>> q;
        for(int i = 0; i < n; i++) {
            int p;
            cin >> p;
            q.push({p,i});
        }

        cout << "Case #" << cas++ << ":";
        while(!q.empty()) {
            auto now = q.top();
            q.pop();
            auto sec = q.top();
            q.pop();
            char c = 'A' + now.second;
            char c2 = 'A' + sec.second;
            if(now.first == sec.first && (q.empty() || sec.first > q.top().first)) {
                cout << " " << c << c2;
                now.first--;
                sec.first--;
                if(now.first) {
                    q.push(now), q.push(sec);
                }
            }
            else {
                cout << " " << c;
                now.first --;
                if(now.first)
                    q.push(now);
                q.push(sec);
            }
        }
        cout << endl;
    }

    return 0;
}
