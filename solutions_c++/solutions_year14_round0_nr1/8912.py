#include <iostream>
#include <map>
#include <vector>

using namespace std;

void solve(int i, int sol1, int sol2, vector<int> v1, vector<int> v2) {
  map<int,int> M;

  int sv1 = 4 * (sol1 - 1);
  for(int i = sv1; i < sv1 + 4; ++i) {
    M[v1[i]]++;
  }
  int sv2 = 4 * (sol2 - 1);
  for(int i = sv2; i < sv2 + 4; ++i) {
    M[v2[i]]++;
  }

  int lasttwo = 0;
  int twocount = 0;

  for(auto it = M.begin(); it != M.end(); ++it) {
    if(it->second > 1) {
      ++twocount;
      lasttwo = it->first;
    }
  }
  
  cout<<"Case #"<<i<<": ";

  if(twocount == 0) {
    cout<<"Volunteer cheated!"<<endl; 
  } else if(twocount > 1) {
    cout<<"Bad magician!"<<endl;
  } else {
    cout<<lasttwo<<endl;
  }
}

int main() {
  int N;
  cin>>N;
  for(int i = 0; i < N; ++i) {
    int sol1, sol2;
    cin>>sol1;
    vector<int> g1(16), g2(16);
    for(int j = 0; j < 16; ++j) {
      cin>>g1[j];
    }
    cin>>sol2;
    for(int j = 0; j < 16; ++j) {
      cin>>g2[j];
    }
    solve(i+1,sol1,sol2,g1,g2);
  }
  return 0;
}
