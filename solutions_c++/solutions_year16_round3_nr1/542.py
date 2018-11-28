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
  int N; cin >> N;
  int P[N];
  for (int i=0; i< N; i++)
    cin >> P[i];
  vector<string> res;
  while (true)
  {
    int i = 0, j = 0;
    while (i < N && P[i] == 0) i++;
    while (j < N && (i == j || P[j] == 0)) j++;
    if (i == N) break;
    string s;
    s += 'A' + i;
    P[i]--;
    if (j != N)
    {
      s += 'A' + j;
      P[j]--;
    }
    res.push_back(s);
  }
  for (int i=res.size()-1; i>=0; i--)
    cout << " " << res[i];
  cout << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ":";
    main2();
  }
}
