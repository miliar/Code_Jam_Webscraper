#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,t1;
	cin>>t;
	t1=t;
	string s;
	while(t!=0)
	{
		cin>>s;
		cout<<"Case #"<<t1-t+1<<": ";
		long long int n=0;
		for(int i=s.length()-1;i>=0;i--)
		{
			if(s[i]=='-' && n%2==0)
			{
				n++;
			}
			if(s[i]=='+' && n%2!=0)
			{
				n++;
			}
		}
		cout<<n<<endl;
		t--;
	}
}
