#include <iostream>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int ca=1; ca<=T; ++ca)
  {
    int l;
    string s;
    cin >> l >> s;
    int pre = 0, add = 0;
    for(int i=0; i<=l; ++i)
    {
      int t = s[i]-'0';
      if (t > 0)
      {
        if (pre+add < i)
          add += i-pre-add;
        pre += t;
      }
    }
    cout << "Case #" << ca << ": " << add << endl;
  }
}
