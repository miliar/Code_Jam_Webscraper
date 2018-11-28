#include<bits/stdc++.h>
using namespace std;
 int main()
 {
     ifstream IF;
     ofstream OF;
     IF.open("input.txt");
     OF.open("output.txt");
int t,l,x,i,k,j,trm,flag,n,ii;
char dtemp,ctemp,btemp;
IF>>t;
string s,temp;
pair<  pair<char,char>, char> p[20];
pair <char,char> str;
p[0] = make_pair(make_pair('1','1'),'1');
p[1] = make_pair(make_pair('1','i'),'i');
p[3] = make_pair(make_pair('1','k'),'k');
p[2] = make_pair(make_pair('1','j'),'j');
p[4] = make_pair(make_pair('i','1'),'i');
p[5] = make_pair(make_pair('i','i'),'1');
p[6] = make_pair(make_pair('i','j'),'k');
p[7] = make_pair(make_pair('i','k'),'j');
p[8] = make_pair(make_pair('j','1'),'j');
p[9] = make_pair(make_pair('j','i'),'k');
p[10] = make_pair(make_pair('j','j'),'1');
p[11] = make_pair(make_pair('j','k'),'i');
p[12] = make_pair(make_pair('k','1'),'k');
p[13] = make_pair(make_pair('k','i'),'j');
p[14] = make_pair(make_pair('k','j'),'i');
p[15] = make_pair(make_pair('k','k'),'1');
for(trm=1;trm<=t;trm++)
{  flag=0;
IF>>l>>x;
IF>>s;
temp=s;
for(i=1;i<x;i++)
{
    s+=temp;
}
dtemp='1';
n=s.length();
 int neg1=0;
for(i=0;i<n;i++)
{
str= make_pair(dtemp,s[i]);
  for(ii=0;ii<16;ii++)
  {
      if(p[ii].first==str)
      {dtemp = p[ii].second;

         if(str==make_pair('i','i')||str==make_pair('j','j')||str==make_pair('k','k')||str==make_pair('i','k')||str==make_pair('j','i')||str==make_pair('k','j'))
                neg1++;
                if(neg1%2==0)
                    neg1=0;
       break;}
  }
  if(dtemp=='i' && neg1%2==0)
  {
    break;

  }}
  if(i==n)
    flag=1;
  else{
        int neg2=0;
      ctemp = '1';
      for(j=i+1;j<n;j++)
      {
          str= make_pair(ctemp,s[j]);
  for(ii=0;ii<16;ii++)
  {
      if(p[ii].first==str)
        {ctemp = p[ii].second;
         if(str==make_pair('i','i')||str==make_pair('j','j')||str==make_pair('k','k')||str==make_pair('i','k')||str==make_pair('j','i')||str==make_pair('k','j'))
                neg2++;
                if(neg2%2==0)
                    neg2=0;
         break;}
  }
          if(ctemp== 'j' && neg2%2==0)
          {
              break;
          }}

          if(j==n)
            flag=1;
          else{
              btemp = '1';
      {int neg3=0;
      for(k=j+1;k<n;k++)
      {
          str= make_pair(btemp,s[k]);
  for(ii=0;ii<16;ii++)
  {
      if(p[ii].first==str)
        {btemp = p[ii].second;
         if(str==make_pair('i','i')||str==make_pair('j','j')||str==make_pair('k','k')||str==make_pair('i','k')||str==make_pair('j','i')||str==make_pair('k','j'))
                neg3++;
                if(neg3%2==0)
                    neg3=0;
           break;}
  }
      }
      if(btemp== 'k' && neg3%2==0)
      {
           OF<<"Case #"<<trm<<": "<<"YES"<<endl;
      }
      else flag=1;

}}}
if(flag==1)
    OF<<"Case #"<<trm<<": "<<"NO"<<endl;

}
IF.close();
OF.close();
return 0;
 }
