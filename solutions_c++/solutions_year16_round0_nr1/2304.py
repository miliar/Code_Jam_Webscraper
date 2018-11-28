#include <iostream>
#include <set>

using namespace std;

set<int> dg;

void addDg(long long l)
{
  while(l)
    {
      int d = l % 10;
      dg.insert(d);
      l /= 10;
    }
}
long long solve(long long n)
{
  if(n == 0)
    return -1;
  long long s = 0;
  while(dg.size() < 10)
  {
    s+=n;
    addDg(s);
    //  cout << dg.size() << endl;
  }
  dg.clear();
  return s;
}
int main()
{
  int t;
  cin >> t;
  for(int i=0; i<t; i++)
    {
      long long n;
      cin >> n;
      long long k = solve(n);
      cout << "Case #"<<i+1<<": ";
      if(k<0)
	cout <<"INSOMNIA";
      else
	cout << k;
      cout << endl;
    }
  return 0;
}
