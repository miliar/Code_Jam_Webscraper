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
  string s; cin >> s;
  int tab['Z' - 'A' + 1];
  for (char i='A'; i<='Z'; i++)
    tab[i - 'A'] = 0;
  
  for (int i=0; i<s.size(); i++)
    tab[s[i] - 'A']++;
  
  vi res;
  while (tab['Z'-'A'])
  {
    tab['Z'-'A']--;
    tab['E'-'A']--;
    tab['R'-'A']--;
    tab['O'-'A']--;
    res.push_back(0);
  }
  while (tab['W'-'A'])
  {
    tab['T'-'A']--;
    tab['W'-'A']--;
    tab['O'-'A']--;
    res.push_back(2);
  }
  while (tab['X'-'A'])
  {
    tab['S'-'A']--;
    tab['I'-'A']--;
    tab['X'-'A']--;
    res.push_back(6);
  }
  while (tab['G'-'A'])
  {
    tab['E'-'A']--;
    tab['I'-'A']--;
    tab['G'-'A']--;
    tab['H'-'A']--;
    tab['T'-'A']--;
    res.push_back(8);
  }
  while (tab['U'-'A'])
  {
    tab['F'-'A']--;
    tab['O'-'A']--;
    tab['U'-'A']--;
    tab['R'-'A']--;
    res.push_back(4);
  }
  while (tab['F'-'A'])
  {
    tab['F'-'A']--;
    tab['I'-'A']--;
    tab['V'-'A']--;
    tab['E'-'A']--;
    res.push_back(5);
  }
  while (tab['H'-'A'])
  {
    tab['T'-'A']--;
    tab['H'-'A']--;
    tab['R'-'A']--;
    tab['E'-'A']--;
    tab['E'-'A']--;
    res.push_back(3);
  }
  while (tab['V'-'A'])
  {
    tab['S'-'A']--;
    tab['E'-'A']--;
    tab['V'-'A']--;
    tab['E'-'A']--;
    tab['N'-'A']--;
    res.push_back(7);
  }
  while (tab['O'-'A'])
  {
    tab['O'-'A']--;
    tab['N'-'A']--;
    tab['E'-'A']--;
    res.push_back(1);
  }
  while (tab['I'-'A'])
  {
    tab['N'-'A']--;
    tab['I'-'A']--;
    tab['N'-'A']--;
    tab['E'-'A']--;
    res.push_back(9);
  }
  
  sort(res.begin(), res.end());
  
  for (auto x : res)
    cout << x;
  cout << endl;
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
