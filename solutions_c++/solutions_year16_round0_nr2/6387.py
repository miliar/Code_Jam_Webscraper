#include <iostream>
using namespace std;

int happy_pancake(string s);
string upsidedown(int size, string s);

int main()
{
  int C; cin>>C;
  for(int i=0; i<C; ++i) {
    string s; cin>>s;
    int count = happy_pancake(s);
    cout<<"Case #"<<i+1<<": "<<count<<endl;
  }
  return 0;
}

int happy_pancake(string s)
{
  int cnt=0;
  int k=s.size();
  while (k--) {
    if (s[k] == '+') continue;

    ++cnt;
    s = upsidedown(k+1, s) + s.substr(k+1, s.size());
  }

  return cnt;
}

string upsidedown(int size, string s)
{
  string r="";
  // or just count next '-'
  for(int i=0; i<size; ++i) {
    r += (s[i] == '+' ? '-' : '+');
  }
  return r;
}