#include <queue>
#include <iostream>
using namespace std;

struct party{
    char c;
    int n;
};

class compare {
public:
    bool operator() (const party &p1, const party &p2) {
        return p1.n <= p2.n;
    }
};

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        priority_queue<party, vector<party>, compare> q;
        int N;
        cin >> N;
        int total = 0;
        for(int j = 0; j < N; ++j) {
            party p;
            p.c = 'A' + j;
            cin >> p.n;
            if(p.n > 0) {
                q.push(p);
            }
            total += p.n;
        }
        cout << "Case #" << i << ": ";
        while(!q.empty()) {
            party p1 = q.top();
            q.pop();
            cout << p1.c;
            --p1.n;
            --total;
            if(!q.empty()) {
                party p2 = q.top();
                if(p1.n > p2.n) {
                    cout << p1.c;
                    --p1.n;
                    --total;
                } else if(p1.n < p2.n && p2.n > total/2) {
                    cout << p2.c;
                    q.pop();
                    --p2.n;
                    --total;
                    if(p2.n > 0) {
                        q.push(p2);
                    }
                }
            }
            if(p1.n > 0) {
                q.push(p1);
            }
            cout << ' ';
        }
        cout << endl;
    }
}