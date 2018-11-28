#include <vector>
#include <map>
#include <iostream>
#include <stdio.h>
#include <assert.h>
#include <set>

using namespace std;

#define DEBUG false
#define DBG(...) if (DEBUG) fprintf(stdout,__VA_ARGS__);

struct Chest {
  int index;
  int type;
  bool locked;
  vector<int> keys;
};

struct State {
  vector<Chest> chests; 
  map<int,int> keys; // keys on hands
  vector<int> open;  // open sequence
  set<vector<bool> > fail;
};

void add_key(int key, State* state)
{
  if (state->keys.find(key) == state->keys.end())
    state->keys[key] = 1;
  else
    state->keys[key]++;
}

void remove_key(int key, State* state)
{
  assert(state->keys.find(key) != state->keys.end());
  assert(state->keys[key] > 0);
  state->keys[key]--;
}
         

void open_chest(State* state, int i)
{
  DBG("open %d\n",i+1);
  Chest& chest = state->chests[i];
  
  assert(chest.locked);
  chest.locked = false;
  assert(state->keys[chest.type] > 0);
  state->keys[chest.type]--;
  for(unsigned int i = 0; i < chest.keys.size(); i++)
    add_key(chest.keys[i],state);
  state->open.push_back(chest.index);
}

void unopen_chest(State* state, int i)
{
  DBG("unopen %d\n",i+1);
  Chest& chest = state->chests[i];

  assert(!chest.locked);
  chest.locked = true;
  state->keys[chest.type]++;
  for(unsigned int i = 0; i < chest.keys.size(); i++)
    remove_key(chest.keys[i],state);
  state->open.pop_back();
}

bool can_open(int chest_type, const map<int,int>& keys)
{
  map<int,int>::const_iterator it;
  it = keys.find(chest_type);
  return (it != keys.end() &&
          it->second > 0);
}

bool all_open(const State& state)
{
  for(unsigned int i = 0; i < state.chests.size(); i++)
    if (state.chests[i].locked)
      return false;
  return true;
}

bool doom_failure(const State& state)
{
  vector<bool> x(state.chests.size());
  for(unsigned int i = 0; i < state.chests.size(); i++)
    x[i] = state.chests[i].locked ;
  return state.fail.find(x) != state.fail.end();
}

void learn_failure(State* state)
{
  vector<bool> x(state->chests.size());
  for(unsigned int i = 0; i < state->chests.size(); i++)
    x[i] = state->chests[i].locked ;
  state->fail.insert(x);
}

bool find_treasure(State* state)
{
  if (all_open(*state))
    return true;

  if (doom_failure(*state))
    return false;

  for(unsigned int i = 0; i < state->chests.size(); i++) {
    Chest& chest = state->chests[i];
    if (chest.locked && can_open(chest.type,state->keys)) {
      open_chest(state,i);
      if (find_treasure(state))
        return true;
      unopen_chest(state,i); // recover
    }
  }

  learn_failure(state);
  
  DBG("fail\n");
  return false;
}


int main()
{
  int n;
  cin >> n;
  for(int k = 1; k <= n; k++) {
    State state;
    int nkeys,nchests;

    cin >> nkeys >> nchests;
    for(int i = 0; i < nkeys; i++) {
      int key;
      cin >> key;
      add_key(key,&state);
    }

    for(int i = 0; i < nchests; i++) {
      Chest chest;
      int nk;
      cin >> chest.type >> nk;
      chest.index = i+1;
      chest.locked = true;
      while(nk--) {
        int kk;
        cin >> kk;
        chest.keys.push_back(kk);
      }
      state.chests.push_back(chest);
    }

    printf("Case #%d: ",k);
    if (find_treasure(&state)) {
      for(unsigned int i = 0; i < state.open.size(); i++)
        printf("%d ",state.open[i]);
    } else {
      printf("IMPOSSIBLE");
    }
    printf("\n");

  }
  return 0;
}

    
