#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main() {
	// your code goes here
	long long q=1,i,t,x,temp,temp1,count,ans;
	string s;
	cin>>t;
	while(t--)
	{
		cin>>x;
		cin>>s;
		temp=s[0]-48;
		//cout<<temp<<endl;
		count=temp;
		ans=0;
		for(i=1;i<s.length();i++)
		{
			temp1=s[i]-48;
			if(i>count && temp1!=0)
			{ans=ans+i-count;
			count=i;
			}count=count+temp1;
		}
		cout<<"Case #"<<q++<<": "<<ans<<endl;
	}
	return 0;
}