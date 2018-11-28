#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

const long long int MOD = 1000002013LL;

struct event {
    long long int people;
    long long int position;
    bool operator<(const event& other) const {
        if (position == other.position) {
            return people > other.people;
        }
        return position < other.position;
    }
};

int main() {

    int T;

    cin >> T;
    for (int t = 1; t <= T; t++) {
        long long int N;
        int M;
        cin >> N >> M;

        vector<event> events;
        vector<int> starts(M);
        vector<int> ends(M);
        vector<int> peoples(M);
        for (int i = 0; i < M; i++) {
            cin >> starts[i] >> ends[i] >> peoples[i];
            event e;
            e.position = starts[i];
            e.people = peoples[i];
            events.push_back(e);
            e.position = ends[i];
            e.people = -peoples[i];
            events.push_back(e);
        }
        sort(events.begin(), events.end());

        long long int expected = 0;
        long long int actual = 0;
        for (int i = 0; i < M; i++) {
            long long int stations = ends[i] - starts[i];
            long long int fare = (N+N-(stations-1)) * (stations) / 2;
            fare %= MOD;
            expected += fare * peoples[i];
            expected %= MOD;
        }

        map<long long int, long long int> current;
        for (int i = 0; i < events.size(); i++) {
            if (events[i].people > 0) {
                current[events[i].position] += events[i].people;
            } else {
                for (map<long long int, long long int>::reverse_iterator it = current.rbegin(); it != current.rend(); it++) {
                    if (it->second >= -events[i].people) {
                        long long int stations = events[i].position - it->first;
                        long long int fare = (N+N-(stations-1)) * (stations) / 2;
                        fare %= MOD;
                        actual += fare * (-events[i].people);
                        actual %= MOD;
                        it->second += events[i].people;
                        break;
                    } else {
                        long long int stations = events[i].position - it->first;
                        long long int fare = (N+N-(stations-1)) * (stations) / 2;
                        fare %= MOD;
                        actual += fare * it->second;
                        actual %= MOD;
                        events[i].people += it->second;
                        it->second = 0;
                    }
                }
            }
        }

        long long int ans = MOD + expected - actual;
        ans %= MOD;
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

