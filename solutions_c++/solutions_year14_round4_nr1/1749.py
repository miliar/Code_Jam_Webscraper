#include<cstdio>
#include<vector>
#include<iostream>
#include<algorithm>
#define s(n) scanf("%d",&n)
using namespace std;
int main()
{
	int t,x,n,i,ca=0,ans,v,j;
	vector<int> p;
	vector<int> st;
	s(t);
	while(t--)
	{
		ca++;
		ans = 0;
		s(n);
		s(x);
		p.clear();
		st.clear();
		for (i=0;i<n;i++)
		{
			s(v);
			p.push_back(v);
			st.push_back(0);
		}
		sort(p.begin(),p.end());
		for (i=n-1;i>=0;i--)
		{
			if (st[i])
				continue;
			st[i] = 1;
			for (j=i-1;j>=0;j--)
			{
				if (st[j]==0 && (p[i]+p[j] <= x))
				{
					st[j] = 1;
					ans++;
					break;
				}
			}
			if (j==-1)
				ans++;
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
