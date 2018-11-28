#include <iostream>
#include <map>
#include <stack>

using namespace std;

#define MOD 1000002013
#define MAX_PAIRS 1000

inline long long cost(long long numStops, long long distance) {
    return ((2*numStops - distance + 1) * distance) / 2;
}

int main() {
    int ncases;
    cin>>ncases;
    for(int caseNum=0; caseNum < ncases; caseNum++) {
        int numStops;
        int numPairs;
        cin>>numStops>>numPairs;
        long long good = 0;
        map<int, long long> stops;
        for(int n=0; n<numPairs; n++) {
            int start, end;
            long long passengers;
            cin>>start>>end>>passengers;
            if(stops.count(start) == 0)
                stops[start] = 0;
            if(stops.count(end) == 0)
                stops[end] = 0;
            stops[start] += passengers;
            stops[end] -= passengers;
            good += ((cost(numStops, end - start) % MOD) * passengers) % MOD;
            good %= MOD;
        }
        long long bad = 0;
        stack<pair<int, long long> > passengers;
        for(map<int, long long>::iterator it = stops.begin(); it != stops.end(); it++) {
            if(it -> second > 0)
                passengers.push(pair<int, long long>(it->first, it->second));
            else if(it -> second < 0) {
                long long left = -(it -> second);
                while(left > 0) {
                    if(passengers.top().second <= left) {
                        bad += ((cost(numStops, (it -> first) - passengers.top().first) % MOD) * passengers.top().second) % MOD;
                        left -= passengers.top().second;
                        passengers.pop();
                    }
                    else {
                        bad += ((cost(numStops, (it -> first) - passengers.top().first) % MOD) * left) % MOD;
                        passengers.top().second -= left;
                        left = 0;
                    }
                    bad %= MOD;
                }
            }
        }
        cout<<"Case #"<<caseNum+1<<": "<<(good + MOD - bad)%MOD<<"\n";
    }
}
