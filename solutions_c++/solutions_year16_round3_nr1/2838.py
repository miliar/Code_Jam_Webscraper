#include <iostream>
#include <queue>
#include <cmath> 

using namespace std;

priority_queue < pair<int,int> > mypq;

int main() {
    int T;
    cin >> T;
    for(int t=0; t<T; t++) {
        cout << "Case #" << t+1 << ": " ;
        int N;
        int total = 0;
        cin >> N; 
        for(int i=0; i<N; i++) {
            int S;
            cin >> S;
            total += S;
            mypq.push(make_pair(S,i));
        }
        while (!mypq.empty()) {
            pair<int,int> p1 = mypq.top();
            mypq.pop();
            pair<int,int> p2 = mypq.top();
            if (mypq.size() == 2 && p1.first == 1 && p2.first == 1) { 
                cout << char('A' + p1.second), total-=1;
            } else if (p1.first >= 2 && p2.first <= (total-2)/2) {
                cout << char('A' + p1.second);
                cout << char('A' + p1.second);
                total -= 2;
                p1.first -= 2;
                if (p1.first != 0)
                    mypq.push(p1);
            } else if (p1.first -1 <= (total-2)/2 && p2.first - 1 <= (total-2)/2) {
                cout << char('A' + p1.second);
                cout << char('A' + p2.second);
                total -=2;
                p1.first -=1;
                p2.first -=1;
                if (p1.first != 0)
                    mypq.push(p1);
                mypq.pop();
                if (p2.first != 0)
                    mypq.push(p2);
            }
            cout << " ";    
        }
        cout << endl;
    }
    return 0;    
}
