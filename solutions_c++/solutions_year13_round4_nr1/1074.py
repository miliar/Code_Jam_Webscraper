#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cassert>

using namespace std;

inline long long pp (int N, int length) {
  long long val = N * length - (length - 1) * length / 2;
  // cout << "pp (" << N << ", " << length << ") = " << val << endl;
  return val;
}

int main () {
  int T;
  cin >> T;

  for (int ii=0; ii<T; ii++) {
    int N, M;
    cin >> N;
    cin >> M;

    set<int> used_stations;
    map<int, int> entriesm;
    map<int, int> exitsm;
    int passengers = 0;
    long long fare_needed = 0;
    int P = 1000002013;
    for (int i=0; i<M; i++) {
      int o, e, p;
      cin >> o;
      cin >> e;
      cin >> p;

      used_stations.insert (o);
      used_stations.insert (e);
      entriesm[o] += p;
      exitsm[e] += p;
      passengers += p;

      fare_needed += (p * pp (N, e - o)) % P;
    }

    int num_effective_stations = used_stations.size ();
    int entries[num_effective_stations];
    int exits[num_effective_stations];
    int stations[num_effective_stations];

    int current_position;
    int i=0;
    for (set<int>::iterator it = used_stations.begin (); it != used_stations.end (); ++it) {
      int station = *it;
      entries[i] = entriesm[station];
      exits[i] = exitsm[station];
      stations[i] = station;
      // cout << "station " << station << ": entries (" << entries[i] << "), exits (" << exits[i] << ")" << endl;
      i += 1;
    }

    vector<pair<int, int> > trip_length_numbers;

    int passengers_routed = 0;
    while (passengers_routed < passengers) {
      int opt_distance = -1;
      int opt_start = -1;
      int opt_end = -1;
      int opt_capacity = -1;

      int current_run_start = -1;
      int current_run_capacity = 0;
      int current_run_slack = 0;
      for (int i=0; i<num_effective_stations; i++) {
        // cout << "AT station " << stations[i] << ", current_run_capacity = " << current_run_capacity << ", current_run_slack = " << current_run_slack << endl;
        // cout << "  entries = " << entries[i] << ", exits = " << exits[i] << ", s[current_run_start] = " << stations[current_run_start] << endl;
        // cout << "BEST opt_capacity = " << opt_capacity << ", from " << stations[opt_start] << " to " << stations[opt_end] << endl;
        bool just_entered = false;
        if (current_run_capacity == 0 && entries[i] > 0) {
          current_run_start = i;
          current_run_capacity = entries[i];
          current_run_slack = 0;
          // cout << "NEW: s[current_run_start] = " << stations[current_run_start] << ", current_run_capacity = " << current_run_capacity << endl;
          just_entered = true;
        }

        if (i >= current_run_start) {
          if (current_run_capacity > 0) {
            if (stations[i] - stations[current_run_start] > opt_distance) {
              opt_distance = stations[i] - stations[current_run_start];
              opt_start = current_run_start;
              opt_end = i;
              opt_capacity = current_run_capacity;
              assert (opt_capacity > 0);
            }
            if (!just_entered)
              current_run_slack += entries[i];
            current_run_slack -= exits[i];
            if (current_run_slack < 0) {
              current_run_capacity += current_run_slack;
              current_run_slack = 0;
            }
            assert (current_run_capacity >= 0);
          } else {
            assert (exits[i] == 0);
          }
        }
      }
      assert (opt_capacity > 0);
      // cout << "opt_distance = " << opt_distance << ", s[opt_start] = " << stations[opt_start] << ", s[opt_end] = " << stations[opt_end] << endl;
      // cout << "opt_capacity = " << entries[opt_start] << ", entries[opt_start] = " << entries[opt_start] << ", exits[opt_end] = " << exits[opt_end] << endl;
      // assert (opt_capacity == min (entries[opt_start], exits[opt_end]));
      entries[opt_start] -= opt_capacity;
      exits[opt_end] -= opt_capacity;
      trip_length_numbers.push_back (make_pair (stations[opt_end] - stations[opt_start], opt_capacity));
      passengers_routed += opt_capacity;
    }

    long long fare_paid = 0;
    for (int i=0; i<trip_length_numbers.size (); i++) {
      int length = trip_length_numbers[i].first;
      int num = trip_length_numbers[i].second;
      fare_paid += num * pp (N, length) % P;
    }

    long long loss = (fare_needed - fare_paid) % P;
    // cout << "fare_needed = " << fare_needed << endl;
    // cout << "fare_paid = " << fare_paid << endl;

    cout << "Case #" << (ii+1) << ": " << loss << endl;
  }

  return 0;
}
