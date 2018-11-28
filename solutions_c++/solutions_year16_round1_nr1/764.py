#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

void main2()
{
  string res;
  string S; cin >> S;
  for (int i=0; i<S.size(); i++)
  {
    string tmp1 = S[i] + res;
    string tmp2 = res + S[i];
    res = max(tmp1, tmp2);
  }
  
  cout << res << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
