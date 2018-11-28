#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

#define MOD 1000002013

struct event {
    bool isOrigin;
    int point;
    int people;
    int index;
    
    event(bool _isOrigin, int _point, int _people, int _index) {
        isOrigin = _isOrigin;
        point = _point;
        people = _people;
        index = _index;
    }
};

typedef struct event event;
typedef pair<int, int> PII;

bool cmp(event e1, event e2) {
    if (e1.point == e2.point) {
        return (e1.index <= e2.index);
    }
    return e1.point <= e2.point;
}

int N;

long long int calFare(int origin, int destination, int people) {
    long long int ns = destination - origin;
    long long int ans = people * ((ns * N - ns * (ns + 1) / 2) % MOD);
    ans %= MOD;
    return ans;
}

void solve() {
    int M;
    cin >> N >> M;
    vector<event> events;
    long long int ans = 0;
    int index0 = 0, index1 = M;
    while (M--) {
        int o, e, p;
        cin >> o >> e >> p;
        events.push_back(event(true, o, p, ++index0));
        events.push_back(event(false, e, p, ++index1));
        ans += calFare(o, e, p);
        ans %= MOD;
    }
    sort(events.begin(), events.end(), cmp);
    priority_queue<PII> pq;
    for (int i=  0; i < events.size(); i++) {
        if (events[i].isOrigin) {
            pq.push(PII(events[i].point, events[i].people));
        } else {
            int people = events[i].people;
            while (people) {
                PII eve = pq.top();
                pq.pop();
                if (eve.second > people) {
                    ans -= calFare(eve.first, events[i].point, people);
                    eve.second -= people;
                    pq.push(eve);
                    people = 0;
                } else {
                    ans -= calFare(eve.first, events[i].point, eve.second);
                    people -= eve.second;
                }
                ans = (ans + MOD) % MOD;
            }
        }
    }
    cout << ans;
}

int main() {
    int testCases;
    cin >> testCases;
    for (int i  = 1; i <= testCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}