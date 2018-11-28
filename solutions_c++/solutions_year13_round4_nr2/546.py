#include<iostream>
#include<algorithm>

using namespace std;

long long n;

int f(long long x)
{
	int nv = 0;
	while (x>0)
	{
		nv++;
		x=(x+1)/2-1;
	}
	return nv;
}

long long worst(long long x)
{
	int nlose = f(x);

	long long ret = 0;	
	for(int i=0;i<n;i++)
	{
		ret <<=1;
		if (i<nlose)
			ret |= 1;
	}
	return ret;
}

long long best(long long x)
{
	int nwin = f(x);

	long long ret = 0;	
	for(int i=0;i<n;i++)
	{
		ret <<=1;
		if (i>=nwin)
			ret |= 1;
	}
	return ret;

}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		long long p;
		
		cin >> n >> p;

		long long N = 1LL<<n;
		long long ans1 = N-1, ans2 = 0;

		long long l = 0, r = N;
		while(r-l>1)
		{
			long long mid = (r+l)/2;
			if (worst(mid)>=p)
				r = mid;
			else
				l = mid;
		}
		ans1 = r-1;

		l = 0; r = N;
		
		while(r-l>1)
		{
			long long mid = (r+l)/2;
			if (best(N-mid-1)<p)
				l = mid;
			else
				r = mid;
		}

		ans2 = l;

		cout<< "Case #" << tt << ": " << ans1 << " " << ans2 << endl;
		//cerr<< "Case #" << tt << ": " << sc << " " << m << endl;
	}
	return 0;
}
