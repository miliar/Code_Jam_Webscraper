#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


int g1(vector<double> a, vector<double> b)
{
	int rs=0, n=a.size();
	vector<int> u(n, 0);
	for (int i=0;i<n;++i)
	{
		int mi=-1;
		for (int j=0;j<n;++j)
		{
			if (u[j]||b[j]<a[i]) continue;
			if (mi==-1||b[mi]>b[j]) mi=j;
		}
		if (mi!=-1)
		{
			u[mi]=1;
			continue;
		}
		++rs;
		for (int j=0;j<n;++j)
		{
			if (u[j]) continue;
			if (mi==-1||b[mi]>b[j]) mi=j;
		}
		u[mi]=1;
	}
	return rs;
}

int g2(vector<double> a, vector<double> b)
{
	int rs=0, i=0, j=0, n=a.size();
	while (i<n)
	{
		while (i<n&&a[i]<b[j]) ++i;
		if (i<n) ++rs;
		++i;
		++j;
	}
	return rs;
}

int main()
{
	int n, t;
	scanf("%d", &t);
	for (int te=0;te<t;++te)
	{
		scanf("%d", &n);
		vector<double> a(n), b(n);
		for (int i=0;i<n;++i) scanf("%lf", &a[i]);
		for (int i=0;i<n;++i) scanf("%lf", &b[i]);
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		printf("Case #%d: %d %d\n", te+1, g2(a, b), g1(a, b));
	}
	return 0;
}