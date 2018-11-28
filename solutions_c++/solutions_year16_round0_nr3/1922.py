#include <iostream>
#include <string>
#include <set>
using namespace std;

set<string> alls;
int oneCase(const string& s, int toDo)
{
  if(alls.find(s)!=alls.end())
    return toDo;
  alls.insert(s);
  cout << s;
  for(int i=3; i<=11; i++)
    cout<<" "<< i;
  cout << endl;
  return toDo-1;
}
int createS(string s, int l, int r, int toDo)
{
  if(toDo==0)
    return 0;
  if(l>r)
    {
      return oneCase(s, toDo);
    }
  //j = createS(s, l+1, r-1, j);
  for(int k=1; l+k<=r && toDo>0; k+=2)
    for(int i=l; i+k <= r && toDo>0; i++)
      {
	toDo = createS(s, i+1, i+k-1, toDo);
	s[i] =s[i+k] = '1';
	//	cout << i<< " -1- " << i+k<<endl;
	toDo = createS(s, i+1, i+k-1, toDo);
	s[i] =s[i+k] = '0';
	//	cout << i<< " -0- " << i+k<<endl;

      }
  return toDo;
}
int main()
{
  int t, n, j;
  cin >> t >> n >> j;
  string s(n-2, '0');;
  s = "1" + s + "1";
  cout << "Case #1:" << endl;
  createS(s, 1, n-2, j);
  // cout << n << endl;
  //cout << s << endl;
  return 0;
}
