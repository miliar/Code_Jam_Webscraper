#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	freopen ("aain.txt","r",stdin);
	freopen ("aaout.txt","w",stdout);
	int tc, n, t=0;
	scanf("%d", &tc);
	
	while(tc--)
	{
		t++;
		scanf("%d", &n);
		float naomi[n], ken[n];
		float _naomi[n], _ken[n];
		for(int i=0;i<n;i++)
		{
			scanf("%f", &naomi[i]);
			_naomi[i]=naomi[i];
		}
		for(int i=0;i<n;i++)
		{
			scanf("%f", &ken[i]);
			_ken[i]=ken[i];
		}
		sort(naomi, naomi+n, greater<float>());
		sort(ken, ken+n, greater<float>());
		sort(_naomi, _naomi+n, greater<float>());
		sort(_ken, _ken+n, greater<float>());
		bool flg;
		int d=0, o=0;
		for(int i=0;i<n;i++)
		{
			flg= true;
			for(int j=0;j<n;j++)
			{
				if(naomi[i]>ken[j]&&ken[j]!=-1)
				{
					d++;
					naomi[i]=ken[j]= -1;
					flg= false;
					break;
				}
			}
			if(flg)
			{
				for(int i=0;i<n;i++)
				if(ken[i]!=-1)
				{
					ken[i]=-1;
					break;
				}
				for(int i=n-1;i>=0;i--)
				if(naomi[i]!=-1)
				{
					naomi[i]=-1;
					break;
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			if(naomi[i]!=-1)
			d++;
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(_naomi[i]<_ken[j])
				{
					_naomi[i]=_ken[j]=-1;
					break;
				}
			}
		}
		for(int i=0;i<n;i++)
		if(_naomi[i]!=-1)
		o++;
		printf("Case #%d: %d %d\n",t, d,o);
	}
	return 0;
}
