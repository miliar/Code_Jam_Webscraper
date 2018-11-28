#include<bits/stdc++.h>
using namespace std;
long int t,i,a[20],j,h;
string s;
map<char,long int>m;
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
     m.clear();
      cinf>>s;
      for(i=0;i<s.size();i++)
            m[s[i]]++;
      a[0]=m['Z'];
      a[2]=m['W'];
      a[4]=m['U'];
      a[6]=m['X'];
      a[8]=m['G'];
      a[1]=m['O']-a[0]-a[2]-a[4];
      a[3]=m['H']-a[8];
      a[5]=m['F']-a[4];
      a[7]=m['S']-a[6];
      a[9]=(m['N']-a[7]-a[1])/2;

      coutf<<"Case #"<<h<<": ";
      for(i=0;i<=9;i++)
      {
          for(j=1;j<=a[i];j++)
            coutf<<i;
      }
      coutf<<endl;
      h++;
  }
    return 0;
}

