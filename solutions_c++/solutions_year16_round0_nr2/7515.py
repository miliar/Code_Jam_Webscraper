#include <bits/stdc++.h>

using namespace std;

int main()
{
	long long int t,j=1,l,k;
	scanf("%lld",&t);
	string s,st,m="+";
	while(j<=t)
	{
		k=0;
		cin >> s;
		l=s.length();
		string st1;
		st1=s[0];
		for(int i=0;i<l;i++)
		{
			st=s[i];
			if(st=="+")
			{
				if(st1=="-")
				{
					st1="+";
					k++;
				}
				//cout << s[i] << i << "\n";
			}
			else
			{
				if(st1=="+")
				{
					st1="-";
					k++;
				}
			}
		}
		if(st1=="-")
			k++;
		printf("Case #%lld: %lld\n",j,k);
		j++;
	}
	return 0;
}