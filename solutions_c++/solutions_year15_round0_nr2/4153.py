#include <iostream>
#include <vector>
#include <queue>
#include <math.h>
#include <set>

using namespace std;

int main() {

    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        std::priority_queue<int, std::vector<int> > pq;
        int D;
        cin >> D;
        for(int d = 0; d < D; d++) {
            int p;
            cin >> p;
            pq.push(p);
        }
        int mn = pq.top();
        for(int i = 1; i < pq.top(); i++) {
            int tp = pq.top();
            pq.pop();
            if(tp == 1) break;
            if(tp == 9) {
                if(pq.empty() || (pq.size() == 1 && pq.top() < 7)) {
                    pq.push(3);
                    pq.push(6);
                } else {
                    if(pq.size() > 1) {
                        int temp = pq.top();
                        pq.pop();
                        if(temp < 7 && pq.top() < 4) {
                            pq.push(3);
                            pq.push(6);
                        } else {
                            pq.push(4);
                            pq.push(5);
                        }
                        pq.push(temp);
                    } else {
                        pq.push(4);
                        pq.push(5);
                    }
                }
            } else {
                pq.push(tp/2);
                pq.push(tp - tp/2);
            }
            mn = min(mn, i + pq.top());
        }

        cout << "Case #" << (t + 1) << ": " << mn << endl;
    }
    return 0;
}
