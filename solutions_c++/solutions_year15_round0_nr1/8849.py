#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stdio.h>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	long long sum, need,T;
	int n;
	string s;
	cin>>T;
	for(int t=0; t<T; t++)
	{
		sum=0; need=0;
		cin>>n;
		cin>>s;
		for(int i=0; i<=n; i++)
		{
			if(s[i]=='0') continue;
			if(i>sum)
			{
				need+=i-sum;
				sum+=i-sum;
			}
			sum+=s[i]-'0';
		}
		cout<<"Case #"<<t+1<<": "<<need<<endl;
	}
	//system("pause");
	return 0;
}