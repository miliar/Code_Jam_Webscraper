#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<string>
using namespace std;
int main()
{
int T,i,n,l,count,count1=0,t1;
string s,x;
cin >> T;
t1=T;
freopen ("myfile2.txt","w",stdout);
while(T--)
{
cin >> n>> s;
l=s.length();
count=0;
count1=0;
for(i=0;i<l;i++)
{
if(count>=n)
break;
if(s[i]-'0'!=0)
{
if(count<i) {
count1+=1;
count+=1;
}
count+=s[i]-'0';
}
if(s[i]-'0'==0)
{
if(count<i)
{
count1+=1;
count+=1;
}
}
}
if(count<n)
{
count1=count1+(n-count);
}
cout << "Case #"<<t1-T<<": "<<count1<<"\n";
}
fclose(stdout);
return 0;
}
