#include <iostream>
#include <vector>
#include <set>

const int n = 4;

int main() {
  int T;
  using std::cin;
  using std::cout;
  using std::cerr;
  cin >> T;
  for(int tcase=1;tcase<=T;++tcase) {
    int s;
    int a[n][n];
    cin >> s;
    for(int i=0;i<n;i++)
      for(int j=0;j<n;j++)
	cin >> a[i][j];
    std::set<int> x(&a[s-1][0], &a[s-1][n]);
    //cerr << s << '\n';
    //for(auto it=x.begin();it!=x.end();++it) cerr << *it << ' '; cerr << '\n';
    cin >> s;
    for(int i=0;i<n;i++)
      for(int j=0;j<n;j++)
	cin >> a[i][j];
    std::vector<int> sol;
    for(int j=0;j<n;j++)
      if(x.count(a[s-1][j]))
	sol.push_back(a[s-1][j]);
    cout << "Case #" << tcase << ": ";
    if(sol.size() == 1)
      cout << sol[0] << '\n';
    else if(sol.size())
      cout << "Bad magician!\n";
    else
      cout << "Volunteer cheated!\n";
  }
}
