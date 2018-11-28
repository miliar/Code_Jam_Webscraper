#include <string>
#include <map>
#include <sstream>
#include<vector>
#include<iostream>
using namespace std;


int main()
{
  int t,ti;

  cin>>t;
  ti=t;

  for(;t>0;t--)
  {

 string s;
 cin>>s;
 vector<int> a(26,0),v(10,0);

 for(int i=0;i<s.size();i++)
 {
 a[s[i]-'A']++;
 }

 v[0]=a['Z'-'A'];
 a['E'-'A']=a['E'-'A']-a['Z'-'A'];
 a['R'-'A']=a['R'-'A']-a['Z'-'A'];
 a['O'-'A']=a['O'-'A']-a['Z'-'A'];
 a['Z'-'A']=0;

 v[2]=a['W'-'A'];
 a['T'-'A']=a['T'-'A']-a['W'-'A'];
 a['O'-'A']=a['O'-'A']-a['W'-'A'];
 a['W'-'A']=0;

 v[4]=a['U'-'A'];
 a['F'-'A']=a['F'-'A']-a['U'-'A'];
 a['O'-'A']=a['O'-'A']-a['U'-'A'];
 a['R'-'A']=a['R'-'A']-a['U'-'A'];
 a['U'-'A']=0;

 v[6]=a['X'-'A'];
 a['S'-'A']=a['S'-'A']-a['X'-'A'];
 a['I'-'A']=a['I'-'A']-a['X'-'A'];
 a['X'-'A']=0;

 v[8]=a['G'-'A'];
 a['E'-'A']=a['E'-'A']-a['G'-'A'];
 a['I'-'A']=a['I'-'A']-a['G'-'A'];
 a['H'-'A']=a['H'-'A']-a['G'-'A'];
 a['T'-'A']=a['T'-'A']-a['G'-'A'];
 a['G'-'A']=0;

 v[1]=a['O'-'A'];
 a['N'-'A']=a['N'-'A']-a['O'-'A'];
 a['E'-'A']=a['E'-'A']-a['O'-'A'];
 a['O'-'A']=0;

 v[3]=a['R'-'A'];
 a['T'-'A']=a['T'-'A']-a['R'-'A'];
 a['E'-'A']=a['E'-'A']-a['R'-'A'];
 a['H'-'A']=a['H'-'A']-a['R'-'A'];
 a['E'-'A']=a['E'-'A']-a['R'-'A'];
 a['R'-'A']=0;

 v[5]=a['F'-'A'];
 a['I'-'A']=a['I'-'A']-a['F'-'A'];
 a['V'-'A']=a['V'-'A']-a['F'-'A'];
 a['E'-'A']=a['E'-'A']-a['F'-'A'];
 a['F'-'A']=0;

 v[7]=a['V'-'A'];

 v[9]=a['I'-'A'];

  cout<<"Case #"<<(ti-t+1)<<": ";

  for(int i=0;i<v.size();i++)
  {

  for(int j=0;j<v[i];j++)
  {
  cout<<i;
  }
  }

  cout<<endl;
  }

    return 0;
}
