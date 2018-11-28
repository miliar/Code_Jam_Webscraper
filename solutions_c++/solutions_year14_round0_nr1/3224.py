#include <iostream>
using namespace std;
void reada(int &h)
{
  int l;
  cin >> l; h=0;
  for(int i=1;i<=4;++i)
    for(int j=1;j<=4;++j)
    {
      int tmp;
      cin >> tmp;
      if(i==l)
        h |= (1<<tmp);
    }
  //cout << h << endl;
}
int main()
{
  int t;
  cin >> t;
  for(int delta=1; delta<=t; ++delta)
  {
    cout << "Case #"<<delta<<": ";
    int h1, h2;
    reada(h1);
    reada(h2);
    if((h1 & h2) == 0)
    {
      cout << "Volunteer cheated!" << endl;
    }
    else
    {
      bool flag=false;
      int htmp = h1 & h2, t=0,ans;
      //cout << htmp << endl;
      while(htmp)
      {
        if(htmp&1)
        {
          if(flag)
          {
            cout << "Bad magician!" << endl;
            break;
          }
          ans=t; flag=true;
        }
        htmp = htmp >> 1; ++t;
      }
      if(!htmp) cout << ans << endl;
    }
  }
  return 0;
}
