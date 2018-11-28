#include <iostream>

#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef long long llong;

struct Event {
   int id;
   llong loc;
   char type;
   Event(int _id, llong _loc, char _type)
      : id(_id), loc(_loc), type(_type) {}
   bool operator<(const Event& e) const {
      if (loc != e.loc) return loc < e.loc;
      if (type != e.type) return type == 'E';
      return id < e.id;
   }
};

llong N;
int M;
llong IN[1004], OUT[1004];
llong P[1004];

llong calc_cost(llong k) {
   return k*N - k*(k-1) / 2;
}

int main(int argc, char* argv[]) {
   ios_base::sync_with_stdio(false); 
   cin.tie(NULL);

   int TC;
   cin >> TC;
   for (int tc = 1; tc <= TC; ++tc) {
      cin >> N >> M;
      vector<Event> events;
      llong orig_cost = 0;
      for (int m = 0; m < M; ++m) {
         cin >> IN[m] >> OUT[m] >> P[m];
         events.push_back( Event(m, IN[m], 'E') );
         events.push_back( Event(m, OUT[m], 'X') );
         orig_cost += calc_cost( OUT[m] - IN[m] ) * P[m];
      }
   // cerr << orig_cost << endl;

      llong new_cost = 0;
      sort(events.begin(), events.end());
      map<llong, llong, greater<llong> > tickets;
      for (int j = 0; j < events.size(); ++j) {
         const Event ev = events[j];
         if (ev.type == 'E') {
            tickets[ ev.loc ] += P[ev.id];
         }
         else {
            llong out = P[ ev.id ];
            while (out > 0) {
               map<llong, llong, greater<llong> >::iterator it = tickets.begin();
               llong mn = min(out, it->second);
               out -= mn;
               it->second -= mn;
               new_cost += calc_cost( ev.loc - it->first ) * mn;
               if (it->second == 0)
                  tickets.erase(it);
            }
         }
      }
      cout << "Case #" << tc << ": " << orig_cost - new_cost << endl;
   }

   return 0;
}
