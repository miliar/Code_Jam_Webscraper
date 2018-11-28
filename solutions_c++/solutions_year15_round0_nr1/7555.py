#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	int m=1;
	while(t--)
	{
		int l;
		scanf("%d",&l);
		string s;
		cin >> s;
		int cnt=0;
		int sum =s[0]-48;
		
		for(int i=1;i<=l;i++)
		{   int n = s[i]-48;
			if((sum < i)&&(s[i]!='0'))
			{   //cout  << sum << "," << i << endl;
				cnt += i-sum;
				sum += (i-sum)+n;
			}
			else
			{
				sum += n;
			}
		}
		printf("Case #%d: %d\n",m++,cnt);
	}
	return 0;
}