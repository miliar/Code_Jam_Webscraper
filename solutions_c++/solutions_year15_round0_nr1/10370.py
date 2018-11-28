#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int k = 1;
	while(k<=t)
	{
		char str[10];
		int n, i;
		cin>>n;
		cin>>str;
		int count = 0;
		int shy = str[0]-'0';
		for(i=1; i<=n; i++)
		{
			if(str[i]>'0' && shy<i)
			{
				count += (i-shy);
				shy += (i-shy);
			}
			shy += str[i] - '0';
		}
		cout<<"Case #"<<k<<": "<<count<<endl;
		k++;
	}
	return 0;
}
