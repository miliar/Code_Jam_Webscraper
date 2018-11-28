#include<iostream>
#include<cstdio>
#include<queue>

using namespace std;

int main()
{
	freopen("in.txt","rt",stdin);
	freopen("Bout.txt","wt",stdout);

	int TC;
	cin>>TC;
	double z = 0;
	
	for(int tc=0;tc<TC;++tc)
	{
		double C,F,X;
		cin>>C>>F>>X;
		double f = 2,a;
		double ans = 1/z;
		queue< pair<double,double> > q;
		q.push( make_pair(0,2) );
		while(q.size())
		{
			f =q.front().second;
			a = q.front().first;
			q.pop();
			ans = min(ans, a+X/f);
			a+=C/f;
			if( a < ans )
				q.push(make_pair(a,f+F));
		}
		printf("Case #%d: %.9f\n",tc+1,ans);
	}
	return 0;
}