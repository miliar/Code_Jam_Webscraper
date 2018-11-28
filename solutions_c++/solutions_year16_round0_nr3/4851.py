#include <bits/stdc++.h>
using namespace std;

#define endl "\n"
typedef long long int ll;

int main()
{
  int t, n, j, teste=1;
  string s;
  vector<pair<int, int> > v;

  cin >> t;
  for(int i = 0; i < t; i++)
  {
    cin >> n >> j;
    v.push_back(make_pair(n, j));
  }
  
  for(int i = 0; i < t; i++)
  {
    n=v[i].first;  j=v[i].second;
    stringstream ss;
    ss << n;
    string filename = "pre/"+ss.str();
    freopen(filename.c_str(), "r", stdin);
    
    cout << "Case #" << teste++ << ":\n";
    while(j--)
    {
      getline(std::cin, s);
      cout << s << endl;
    }
    fclose(stdin);
  }
  
  return 0;
}
