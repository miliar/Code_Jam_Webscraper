#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int sum=0;
	
	string s[t];
	int pan[100]={0};
	
	for (int i=0;i<t;i++)
	cin>>s[i];
	
	for (int i=0;i<t;i++)
	{
		sum=0;
		
		for (int j=0;j<s[i].length()-1;j++)
		{
			if (s[i][j]!=s[i][j+1]) sum++;
		}
		if (s[i][s[i].length()-1] =='-') sum++;
		
		cout<<"Case #"<<i+1<<": "<<sum<<endl;
	}
}
