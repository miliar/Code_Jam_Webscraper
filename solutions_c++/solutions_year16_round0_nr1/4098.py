#include<bits/stdc++.h>
using namespace std;
int main()
{
	ifstream file1("A-large.in");
	ofstream file2("file13.txt");
	int t;
	file1>>t;
	for(int j=0;j<t;j++)
	{
		long long int n;
		file1>>n;
		file2<<"Case #"<<j+1<<": ";
		if(n==0) file2<<"INSOMNIA\n";
		else
		{
			int ans;
			string str="0000000000";
			for(int i=1;str!="1111111111";i++)
			{
				long long int m=n*i;
				ans=m;
				//cout<<m<<" "<<str<<endl;
				while(m>0) {str[m%10]='1';m/=10;}
			}
			file2<<ans<<endl;
		}
	}
}
