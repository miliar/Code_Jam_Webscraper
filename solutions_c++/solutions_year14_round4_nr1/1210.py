#include <iostream>
#include <set>
using namespace std;

int N, T;
multiset<int> st;

void scan(){
  st.erase(st.begin(), st.end());
  
  cin >> N >> T;
  
  for(int i = 0; i < N; ++i){
    int x;
    cin >> x;
    st.insert(x);
  }
}

void solve(int testCase){
  cout << "Case #" << testCase << ":";
  int res = 0;
  while(st.size()){
    set<int> :: iterator tt = st.lower_bound(T - *st.begin() + 1);
    if(tt == st.begin()){
      ++res;
      st.erase(st.begin());
      continue;
    }
    --tt;
    if(tt == st.begin()){
      ++res;
      st.erase(st.begin());
      continue;
    }
    st.erase(st.begin());
    st.erase(tt);
    ++res;
  }
  cout << " "<< res << endl;
}
int main(){
  int tests;
  
  cin >> tests;
  
  for(int i = 1; i <= tests; ++i){
    scan();
    solve(i);
  }
}
