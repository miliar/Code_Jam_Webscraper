#include <iostream>
#include <math.h>
#include <sstream>
#include <string>
using namespace std;
bool issquare(int i)
{
	int x=sqrt(i);
	return ((x*x)==i);
}
bool ispallindrome(int i)
{
	string str = static_cast<ostringstream*>( &(ostringstream() << i) )->str();
	
	int l=str.length();
	int len=l/2;
	int k;
	for(k=0;k<=len;k++)
	{
		if(str[k]!=str[l-k-1])
			break;
	}
	return (k==len+1);
	
}
int main()
{
	int a,b,t,t2,i,count;
	cin>>t;
	t2=t;
	while(t2--)
	{
		count=0;
		cin>>a>>b;
		for(i=a;i<=b;i++)
		if(issquare(i) && ispallindrome(i) && ispallindrome(sqrt(i)))
		{
			//cout<<i<<"\t";
			count++;
		}
		cout<<"Case #"<<t-t2<<": "<<count<<endl;
	}
}
