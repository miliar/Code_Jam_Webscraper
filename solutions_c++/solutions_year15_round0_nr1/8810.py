#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("E://A-large.in","r",stdin);
	freopen("E://t1.txt","w",stdout);
	int ct = 0;
	int t,s,sum;
	string str;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		cin>>s>>str;
		ct = 0;
		sum = 0;
		int l = str.length();
		for(int i=0;i<l;i++)
		{
			if(i > sum)
			{
				ct += (i - sum);
				sum += (i - sum);
			}
			sum += ((int)str[i] - '0');
		//	cout<<sum<<endl;
		}	
		printf("Case #%d: %d\n",j,ct);
	}
}
