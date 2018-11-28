#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

class Chest {
public:
  Chest(int t_, vector<int>& k_) : type(t_), keys(k_) {}
  int type;
  vector<int> keys;
};

vector<int> solve(const multiset<int>&, const vector<Chest>&);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    int K, N;
    cin >> K >> N;
    multiset<int> keys;
    for(int j = 0; j < K; j++) {
      int tmp;
      cin >> tmp;
      keys.insert(tmp);
    }
    vector<Chest> chests;
    for(int j = 0; j < N; j++) {
      int t, num;
      vector<int> inside_keys;
      cin >> t >> num;
      for(int k = 0; k < num; k++) {
	int ik;
	cin >> ik;
	inside_keys.push_back(ik);
      }
      chests.push_back(Chest(t,inside_keys));
    }
    vector<int> r = solve(keys, chests);
    if(r.size() == 0) {
      cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << i+1 << ":";
      for(int j = 0; j < r.size(); j++) cout << " " << r[j] + 1;
      cout << endl;
    }
  }
}

vector<int> solve1(multiset<int> keys,
		   set<int> to_solve,
		   const vector<Chest>& chests,
		   map<pair<multiset<int>, set<int> >,
		       vector<int> >& memo) {
  map<pair<multiset<int>, set<int> >, vector<int> >::iterator i;
  multiset<int>::iterator j;
  if((i = memo.find(make_pair(keys, to_solve))) != memo.end()) {
    return i->second;
  } else {
    if(to_solve.size() == 1) {
      int chest_id = *to_solve.begin();
      Chest chest = chests[chest_id];
      if(keys.find(chest.type) != keys.end()) {
	vector<int> v;
	v.push_back(chest_id);
	memo.insert(make_pair(make_pair(keys, to_solve), v));
	return v;
      } else {
	vector<int> v;
	memo.insert(make_pair(make_pair(keys, to_solve), v));
	return v;
      }
    } else {
      for(j = to_solve.begin(); j != to_solve.end(); j++) {
	int chest_id = *j;
	Chest chest = chests[chest_id];
	if(keys.find(chest.type) != keys.end()) { // OK, this can be opend
	  set<int> next_solve = to_solve;
	  next_solve.erase(next_solve.find(*j));
	  multiset<int> next_keys = keys;
	  next_keys.erase(next_keys.find(chest.type));
	  for(int k = 0; k < chest.keys.size(); k++) 
	    next_keys.insert(chest.keys[k]);
	  vector<int> v = solve1(next_keys, next_solve, chests, memo);
	  if(v.size() == 0) continue;
	  else {
	    v.push_back(chest_id);
	    memo.insert(make_pair(make_pair(keys, to_solve), v));
	    return v;
	  }
	} else { // NO, this cannot be opend
	  continue;
	}
      }
      // this key/solve pair cannot be solved
      vector<int> v;
      memo.insert(make_pair(make_pair(keys, to_solve), v));
      return v;
    }
  }
}

vector<int> solve(const multiset<int>& keys, const vector<Chest>& chests) {
  // pair<keyset, chestset> -> solution
  map<pair<multiset<int>, set<int> >, vector<int> > memo;
  set<int> to_solve;
  for(int i = 0; i < chests.size(); i++) to_solve.insert(i);
  vector<int> r = solve1(keys, to_solve, chests, memo);
  reverse(r.begin(), r.end());
  return r;
}
