#include <bits/stdc++.h>
#define lld long long int
using namespace std;

int main() {
	// your code goes here
	ios_base::sync_with_stdio(0);
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		lld max;
		cin>>max;
		int x0,x,i;
		lld sum1=0,sum=0;
		string s;
		cin>>s;
		x0=s[0]-48;
		int t1=1;
		sum+=x0;
		for(i=1;i<=max;i++)
		{
			x0=s[i]-48;
			if(sum<t1)
			{
				sum1+=t1-sum;
				sum+=t1-sum;
			}
			t1++;
			sum+=x0;
		}
		cout<<"Case #"<<k<<": "<<sum1<<endl;
	}
	return 0;
}
