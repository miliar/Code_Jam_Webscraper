#include <iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	int a[105];
	for(int i=0;i<t;i++)
	{
		string s;
		cin>>s;
		int l=s.length();
		if(s.at(0)=='-')
		{
			a[0]=1;
		}
		else
		{
			a[0]=0;
		}
		//cout<<a[0]<<endl;
		for(int j=1;j<l;j++)
		{
			if(s.at(j)=='+')
			{
				a[j]=a[j-1];
			}
			else
			{
				if(s.at(j-1)=='-')
				{
					a[j]=a[j-1];
				}
				else
				{
					a[j]=a[j-1]+2;
				}
			}
			//cout<<a[j]<<endl;
		}
		cout<<"Case #"<<(i+1)<<": "<<a[l-1]<<endl;
	}
	return 0;
}