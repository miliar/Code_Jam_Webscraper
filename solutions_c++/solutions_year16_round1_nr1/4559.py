#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<list>
#include<cstring>
using namespace std;

char ch[100];
int n;
std::list<std::string> mylist;

void makeStr(string res,int index,int len)
{
if(len==n)
 {
  mylist.push_back(res);  
  return ;
 }
 makeStr(ch[index]+res,index+1,len+1);
 makeStr(res+ch[index],index+1,len+1);
}


int main()
{
std::list<std::string>::iterator itr;
ifstream it;
ofstream ot;
it.open("B-large.in");
ot.open("one-output.out");
long int j,t,i,k,c;

it>>t;
for(k=1;k<=t;k++)
{
 ch[0]='\0';
 it>>ch;
 n=strlen(ch);
 makeStr("",0,0);

 mylist.sort();
 itr=mylist.end();
 itr--;
  
  ot<<"Case #"<<k<<": "<<*itr<<"\n";
 // ot<<"Case #"<<k<<": "<<c<<"\n";
 mylist.clear();

}// tst case
it.close();
ot.close();
return 0;
}
