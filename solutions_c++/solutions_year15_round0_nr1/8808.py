#include <bits/stdc++.h>
using namespace std;
int main()
{
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);
	freopen("E://A-large.in","r",stdin);
	freopen("E://t2.txt","w",stdout);
	int count_of_num = 0;
	int t,s,till_sum;
	string str;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		cin>>s>>str;
		count_of_num = 0;
		till_sum = 0;
		int l = str.length();
		for(int i=0;i<l;i++)
		{
			if(i > till_sum)
			{
				count_of_num += (i - till_sum);
				till_sum += (i - till_sum);
			}
			till_sum += ((int)str[i] - '0');
		}	
		printf("Case #%d: %d\n",j,count_of_num);
	}
}
