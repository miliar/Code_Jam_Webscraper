#include <bits/stdc++.h>
using namespace std;
int t,i,l,d1,d3,h;
string s,s2;
int main()
{
  ifstream cinf;
  ofstream coutf;
  cinf.open("input.txt");
  coutf.open("ans.txt");
    cinf>>t;
    h=1;
    while(t--)
    {
      s2.clear();
        cinf>>s;
        l=s.size();
         d1=s[0]-64;
         s2.insert(0,1,s[0]);
        for(i=1;i<l;i++)
        {
            d3=s[i]-64;
            if(d3>=d1)
              {
                  s2.insert(0,1,s[i]);
                  d1=s[i]-64;
              }
              else
                  {
                      s2.insert(s2.size(),1,s[i]);
                  }
        }
           coutf<<"Case #"<<h<<": "<<s2<<endl;
           h++;
    }
    return 0;
}

