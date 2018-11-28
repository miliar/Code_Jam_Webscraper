#include<bits/stdc++.h>
using namespace std;
#define ll long long 
int main()
{
     ll t,o=0;
     string st;
     cin>>t;
     while(t--)
     {o++;
          cin>>st;
          ll n=st.size();
          int hash[26];
          int count[10];
          for(int i=0;i<10;i++)
          count[i]=0;
          for(int i=0;i<26;i++)
          hash[i]=0;
          for(int i=0;i<n;i++)
          hash[st[i]-'A']++;
          if(hash['G'-'A']>0)
          {
               count[8]+=hash['G'-'A'];
               hash['E'-'A']-=hash['G'-'A'];
               hash['I'-'A']-=hash['G'-'A'];
               hash['H'-'A']-=hash['G'-'A'];
               hash['T'-'A']-=hash['G'-'A'];
               hash['G'-'A']-=hash['G'-'A'];
          }
          if(hash['Z'-'A']>0)
          {
                count[0]+=hash['Z'-'A'];
               hash['O'-'A']-=hash['Z'-'A'];
               hash['R'-'A']-=hash['Z'-'A'];
               hash['E'-'A']-=hash['Z'-'A'];
               hash['Z'-'A']-=hash['Z'-'A'];
          }
          if(hash['W'-'A']>0)
          {
               count[2]+=hash['W'-'A'];
               hash['T'-'A']-=hash['W'-'A'];
               hash['O'-'A']-=hash['W'-'A'];
               hash['W'-'A']-=hash['W'-'A'];
          }
          if(hash['U'-'A']>0)
          {
                 count[4]+=hash['U'-'A'];
               hash['O'-'A']-=hash['U'-'A'];
               hash['F'-'A']-=hash['U'-'A'];
               hash['R'-'A']-=hash['U'-'A'];
               hash['U'-'A']-=hash['U'-'A'];
          }
          if(hash['X'-'A']>0)
          {
               count[6]+=hash['X'-'A'];
               hash['S'-'A']-=hash['X'-'A'];
               hash['I'-'A']-=hash['X'-'A'];
               hash['X'-'A']-=hash['X'-'A'];
          }
          if(hash['O'-'A']>0)
          {
                 count[1]+=hash['O'-'A'];
               hash['N'-'A']-=hash['O'-'A'];
               hash['E'-'A']-=hash['O'-'A'];
               hash['O'-'A']-=hash['O'-'A'];
          }
          if(hash['R'-'A']>0)
          {
               count[3]+=hash['R'-'A'];
               hash['E'-'A']-=hash['R'-'A'];
               hash['E'-'A']-=hash['R'-'A'];
               hash['H'-'A']-=hash['R'-'A'];
               hash['T'-'A']-=hash['R'-'A'];
               hash['R'-'A']-=hash['R'-'A'];
          }
          if(hash['F'-'A']>0)
          {
               count[5]+=hash['F'-'A'];
               hash['E'-'A']-=hash['F'-'A'];
               hash['I'-'A']-=hash['F'-'A'];
               hash['V'-'A']-=hash['F'-'A'];
               hash['F'-'A']-=hash['F'-'A'];
          }
          if(hash['S'-'A']>0)
          {
               count[7]+=hash['S'-'A'];
               hash['E'-'A']-=hash['S'-'A'];
               hash['V'-'A']-=hash['S'-'A'];
               hash['E'-'A']-=hash['S'-'A'];
               hash['N'-'A']-=hash['S'-'A'];
               hash['S'-'A']-=hash['S'-'A'];
          }
          if(hash['I'-'A']>0)
          {
               count[9]+=hash['I'-'A'];
               hash['E'-'A']-=hash['I'-'A'];
               hash['N'-'A']-=hash['I'-'A'];
               hash['N'-'A']-=hash['I'-'A'];
               hash['I'-'A']-=hash['I'-'A'];
          }
          cout<<"Case #"<<o<<": ";
          for(int i=0;i<10;i++)
          {
               for(int j=0;j<count[i];j++)
               cout<<i;
          }
          cout<<"\n";
     }
}