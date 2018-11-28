#include <iostream>
#include <algorithm>
using namespace std;

struct event {
    long long time;
    long long passengers;
};

bool operator<(event a, event b) {
    return a.time < b.time;
}

long long N;
event entrances[1000];
event exits[1000];

long long costbetween(long long first, long long second) {
    long long diff = second - first;
    return (N*diff - (diff*(diff-1))/2)%1000002013;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int M;
        cin >> N >> M;
        long long ans = 0;
        for (int i = 0; i < M; i++) {
            long long start, stop, passengers;
            cin >> start >> stop >> passengers;
            entrances[i].time = start;
            exits[i].time = stop;
            entrances[i].passengers = exits[i].passengers = passengers;
            ans = (ans + costbetween(start, stop) * passengers)%1000002013;
        }
        sort(entrances, entrances+M);
        sort(exits, exits+M);
        int entsused = 0;
        for (int i = 0; i < M; i++) {
            while (entsused < M && entrances[entsused].time <= exits[i].time) entsused++;
            for (int j = entsused-1; j >= 0; j--) {
                long long passengers = min(exits[i].passengers, entrances[j].passengers);
                ans = (ans + (1000002013 - costbetween(entrances[j].time, exits[i].time))*passengers)%1000002013;
                exits[i].passengers -= passengers;
                entrances[j].passengers -= passengers;
            }
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }
    return 0;
}
