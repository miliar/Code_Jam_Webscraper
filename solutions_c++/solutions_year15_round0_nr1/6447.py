#include <iostream>
#include<cstring>
using namespace std;

int main() 
{
int t;
cin>>t;
for(int q=0;q<t;q++)
{
int smax;
long count=0;
string s;
cin>>smax;
cin>>s;
long sum=0;
for(int i=0;i<smax;i++)
{
sum+=(s[i]-48); 
if(i+1>sum && count<(i+1-sum)) count=(i+1-sum);
}
cout<<"Case #"<<q+1<<": "<<count<<endl;
}
	return 0;
}
