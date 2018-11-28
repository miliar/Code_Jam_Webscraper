#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int n;
  cin>>n;
  for (int a=1;a<=n;a++)
  {
    cout<<"Case #"<<a<<": ";
    string s;
    cin>>s;
    int f=0;
    bool g=0;
    while (!g)
    {
      g=1;
    for (int i=0;i<s.size();i++)
      if (s[i]=='-')
        g=0;
    if (g)
    {
      cout<<f<<endl;
      break;
    }
      f++;
      string t="";
      int last;
      for (int i=s.size()-1;i>=0;i--)
        if (s[i]=='+')
          t=t+"+";
        else
        {
          last=i;
          break;
        }
      if (s[0]=='-')
      {
        string u="";
        for (int i=last;i>=0;i--)
          if (s[i]=='+')
            u=u+'-';
          else
            u=u+'+';
        t=u+t;
      }
      else
      {
        int u=0;
        while (s[u]=='+')
          u++;
        for (int i=0;i<u;i++)
          s[i]='-';
        t=s;
      }
      s=t;
      //cout<<s<<endl;
    }
  }
  return 0;
}

/*
+--+
---+
++++


++-+
---+
++++

++++-
----+
+++++

++-+-
---+-
+-+++
--+++
+++++
*/