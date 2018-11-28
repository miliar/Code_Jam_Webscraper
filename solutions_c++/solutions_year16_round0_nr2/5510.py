#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<cstring>
using namespace std;


int main()
{
bool flag;
ifstream it;
ofstream ot;
it.open("B-large.in");
ot.open("one-output.out");
long int j,t,i,k,n,c;
char ch[109];
it>>t;
for(k=1;k<=t;k++)
{
 it>>ch;
 n=strlen(ch);
 c=0;i=0;
 if(ch[0]=='-')
  {
  c=1;
  for(i=1;i<n;i++)
   if(ch[i]=='+')
     break;
  }
 //cout<<"i +:"<<i<<"\n";
 for(i;i<n;i++)
   {
    if(ch[i]=='-')
      {
	c+=2;
	  for(;i<n;i++)
	   if(ch[i]=='+')
	     break;
      }
   }
 // cout<<"Case #"<<k<<": "<<c<<"\n";
  ot<<"Case #"<<k<<": "<<c<<"\n";


}// tst case
it.close();
ot.close();
return 0;
}
