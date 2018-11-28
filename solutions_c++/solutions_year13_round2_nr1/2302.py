
#include<iostream>
#include<sstream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<algorithm>


int solve(long A, std::vector<long>& list, int i) {
  if (list.size() == i) return 0;

  long m = list[i];
  if (A > m) {
    return solve(A+m, list, i+1);
  } else if (A+A-1 > m) {
    return solve(A+A-1+m, list, i+1) + 1;
  } else if (A == 1) {
    return solve(A, list, i+1) + 1;
  } else if (list.size()-1 == i) {
    return 1;
  } else {
    int ans_if_add = solve(A+A-1, list, i) + 1;
    int ans_if_rem = solve(A, list, i+1) + 1;
    return std::min(ans_if_add, ans_if_rem);
  }
}

int main() 
{
  using namespace std;

  int T = 0;
  cin >> T;

  std::string str;
  getline(cin, str);

  int i = 0;
  for (i=1;i<=T;i++) 
  {
    long A = 0;
    int N = 0;

    cin >> A;
    cin >> N;
    vector<long> list;

    while(N-->0) {
      long m = 0;
      cin >> m;
      list.push_back(m);
    }
    sort(list.begin(), list.end());

    int ans = solve(A, list, 0);

    // Print answer
    cout << "Case #" << i << ": " << ans;
    cout << endl;
  }
}

