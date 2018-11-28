#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

bool check(long k, int dig)
{
  stringstream ss;
  ss << k;
  string s = ss.str();
  return any_of(s.begin(), s.end(), [&](char c){return (c == ('0'+dig));});
}

void tick()
{
  long k0;
  cin >> k0;
 
  if (k0 == 0)   {cout << "INSOMNIA" << endl; return;}

  bool seen[10];
  fill(seen, seen+10, false);
  long k=0;
  while (any_of(seen, seen+10*sizeof(bool), [](bool b){return !b;}))
  {
    k += k0;
    for (int i=0; i < 10; i++)  {if (!seen[i])  {seen[i] = check(k, i);}}
  }
  cout << k  << endl;
}

int main()
{
  int bigN;
  cin >> bigN;
  for (int i=0; i < bigN; i++)
  {
    cout << "Case #" << (i+1) << ": ";
    tick();
  }
}
