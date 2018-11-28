#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

map<int, int> mem;

int mini(int a, int b) {
  if (a == -1) return b;
  if (b == -1) return a;
  if (a < b) return a;
  return b;
}

int solve(int mote_size, vector<int> motes, int index) {

  if (index >= motes.size()) {
    return 0;
  }
  
  //if (mem.find(index) != mem.end()) {
  //return mem[index];
  //}

  if (mote_size > motes[index]) {
    mote_size += motes[index];
    int result = solve(mote_size, motes, index+1);
    return solve(mote_size, motes, index+1);
  }

  //Create mote
  int new_mote_size = mote_size;
  int num_adds = 0;

  if (new_mote_size != 1) {
    while (new_mote_size <= motes[index]) {
      new_mote_size = new_mote_size * 2 - 1;
      num_adds++;
    }
  }
  
  int add_value = -1, delete_value = -1;

  if (new_mote_size > motes[index]) {
    new_mote_size += motes[index];
    add_value = solve(new_mote_size, motes, index+1);
    
    if (add_value != -1) add_value += num_adds;
  }
  
  delete_value = solve(mote_size, motes, index+1);

  if (delete_value != -1) delete_value += 1;
  
  //mem[index] = mini(add_value, delete_value);

  return mini(add_value, delete_value);
}

int main(int argc, char *argv[]) {
  int n_cases;
  cin >> n_cases;

  for (int i = 0; i < n_cases; i++) {
    int mote_size;
    cin >> mote_size;
    
    int num_motes;
    cin >> num_motes;

    vector<int> motes;

    for (int j = 0; j < num_motes; j++) {
      int nmote;
      cin >> nmote;
      
      motes.push_back(nmote);
    }

    sort(motes.begin(), motes.end());

    cout << "Case #" << i+1 << ": " << solve(mote_size, motes, 0) << endl;

    mem.clear();
  }
}
