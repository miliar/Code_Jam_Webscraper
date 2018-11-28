#include<iostream>
#include<string>
#include<cstdio>
typedef long long ll;

using namespace std;

int main(int argc, char *argv[])
{
	ll n,t,i,count,diff,j;
	string s1;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	j=1;
	while(t--)
	{
		cin>>n>>s1;
		count = 0;
		diff = 0;
		count = count + (s1[0]-48);
		for(i=1;i<n+1;i++)
		{
			if(count<i)
			{
				diff = diff + (i-count);
				count = count + (i-count);
			}
			count = count + (s1[i]-48);
		}
		cout<<"Case #"<<j<<": "<<diff<<endl;
		j++;
	}
	return 0;
}
