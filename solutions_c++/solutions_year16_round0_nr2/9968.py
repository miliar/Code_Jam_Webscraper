#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t,i,j,c,f;
	string s;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>s;
		int n= s.length();
		//cout<<n<<endl;
		f=c=0;
		for(j=n-1;j>=0;j--)
		{
			if(s[j]=='+' && f==1)
			{
				f=0;
				c++;
			}	
			else if(s[j]=='-'&&f==0) {
				f=1;
				c++;
			}
		}	
		cout<<"Case #"<<i<<": "<<c<<endl;
	}
	return 0;
}	