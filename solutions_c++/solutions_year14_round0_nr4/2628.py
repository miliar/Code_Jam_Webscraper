#include <cstdio>
#include <set>

void read(int n, std::set<double>& set)
{
	for (int i=0; i<n; ++i)
	{
		double w;
		scanf("%lf", &w);
		set.insert(w);
	}
}

int point(const std::set<double>& mine, const std::set<double>& yours)
{
	std::set<double> yoursCopy(yours);

	int pt = 0;
	
	for (double d : mine)
	{
		auto it = yoursCopy.lower_bound(d);
		if (it != yoursCopy.begin())
		{
			yoursCopy.erase(--it);
			++pt;
		}
	}
	
	return pt;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int cn=1; cn<=t; ++cn)
	{
		int n;
		scanf("%d", &n);
		
		std::set<double> nset, kset;
		read(n, nset);
		read(n, kset);

		printf("Case #%d: %d %d\n", cn, point(nset, kset), n - point(kset, nset));
	}
	
	return 0;
}