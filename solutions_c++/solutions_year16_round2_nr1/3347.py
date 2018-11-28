#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<string>
#include<cstring>
using namespace std;
string s;

bool search(string ch){
int n=ch.length();
string str=s;
int i,j=0;
int index;
for( i=0;i<n;i++)
 {
  index=str.find(ch[i]);
  if(index != std::string::npos)
   {	
        str[index]='Q';	
//	cout<<"pos "<<index<<"\n";
	//ar[j]=index;j++;
   }
  else
	break;
 }
if(i==n)
 {
//  for(i=0;i<j;i++)
//   s[ar[i]]='Q';
  s=str;
//  cout<<"s"<<s<<"\n";
  return true;
 }
else
  return false;
}

int main()
{
bool flag;
ifstream it;
ofstream ot;

char ch[10][10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
it.open("A-large.in");
ot.open("one-output.out");
long int j,t,i,k;
long int n,temp,temp1;
it>>t;
for(k=1;k<=t;k++)
{
 it>>s;
 vector<int> list;
 n=s.length();
// bool flag=true;
 bool findf=true;
 while(findf)
 {
  findf=false;
	if(search("ZERO"))
	{
           list.push_back(0);
	   findf=true;
	}
//cout<<"0\n";
 }
  findf=true;

 while(findf)
 {
  findf=false;
	if(search("TWO"))
	{
           list.push_back(2);
	   findf=true;
	}
 }
  findf=true;

while(findf)
 {
  findf=false;
	if(search("SIX"))
	{
           list.push_back(6);
	   findf=true;
	}
 }
  findf=true;

while(findf)
 {
  findf=false;
	if(search("EIGHT"))
	{
           list.push_back(8);
	   findf=true;
	}
 }

  findf=true;

while(findf)
 {
  findf=false;
	if(search("FOUR"))
	{
           list.push_back(4);
	   findf=true;
	}
 }
  findf=true;

while(findf)
 {
  findf=false;
	if(search("ONE"))
	{
           list.push_back(1);
	   findf=true;
	}
 }
  findf=true;

while(findf)
 {
  findf=false;
	if(search("THREE"))
	{
           list.push_back(3);
	   findf=true;
	}
 }
  findf=true;

while(findf)
 {
  findf=false;
	if(search("FIVE"))
	{
           list.push_back(5);
	   findf=true;
	}
 }
  findf=true;

while(findf)
 {
  findf=false;
	if(search("SEVEN"))
	{
           list.push_back(7);
	   findf=true;
	}
 }
  findf=true;
while(findf)
 {
  findf=false;
	if(search("NINE"))
	{
           list.push_back(9);
	   findf=true;
	}
 }
// cout<<list;
 sort(list.begin(),list.end());
 ot<<"Case #"<<k<<": ";
 for(i=0;i<list.size();i++)
   ot<<list[i];

 ot<<"\n";
}// tst case
it.close();
ot.close();
return 0;
}
