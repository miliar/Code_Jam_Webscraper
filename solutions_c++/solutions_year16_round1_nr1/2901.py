#include<iostream>
#include<string>
using namespace std;
int main(){
	string str,ans;
	int t;
	cin>>t;
	
	for(int i=0;i<t;i++)
	{
		cin>>str;
		ans=str[0];
		for(int j=1;j<str.size();j++)
		{
			if(str[j]<ans[0])
			{
				ans=ans+str[j];
			}
			else
			{
				ans=str[j]+ans;
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
