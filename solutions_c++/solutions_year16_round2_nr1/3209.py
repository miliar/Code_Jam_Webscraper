#include<iostream>
#include<string>
using namespace std;
void remov (string &tel,char ch, int n)
{
 for(int i=0;i<n;i++)
 {
  tel.erase(tel.find(ch));
 }
}
void remov (string &tel,char ch)
{
 tel.erase(tel.find(ch),1);
 }
int main()
{
string s[10];
s[1]="ONE";
s[2]="TWO";
s[3]="THREE";
s[4]="FOUR";
s[5]="FIVE";
s[6]="SIX";
s[7]="SEVEN";
s[8]="EIGHT";
s[9]="NINE";
s[0]="ZERO";
int T;
cin>>T;
for(int p=0;p<T;p++)
{
 int num[10];
for(int i=0;i<10;i++){num[i]=0;}
string tel;
cin>>tel;
for(string::iterator it=tel.begin();it!=tel.end();it++)
{
 if(*it=='Z')++num[0];
 else if(*it=='W')++num[2];
 else if(*it=='U')++num[4];
 else if(*it=='X')++num[6];
 else if(*it=='G')++num[8];
}
for(int i=0;i<9;i+=2){
 for(int j=0;j<num[i];j++){
  for(string::iterator it=s[i].begin();it!=s[i].end();it++){remov(tel,char(*it));}
 }
}
for(string::iterator it=tel.begin();it!=tel.end();it++)
{
 if(*it=='O')++num[1];
 else if(*it=='T')++num[3];
 else if(*it=='F')++num[5];
 else if(*it=='S')++num[7];
}
for(int i=1;i<8;i+=2){
 for(int j=0;j<num[i];j++){
  for(string::iterator it=s[i].begin();it!=s[i].end();it++){remov(tel,char(*it));}
 }
}
num[9]=((tel.size())/4);
cout<<"Case #"<<p+1<<": ";
for(int i=0;i<10;i++)
{
 for(int j=0;j<num[i];j++)
 {
  cout<<i;
 }
}
cout<<endl;
}
}
