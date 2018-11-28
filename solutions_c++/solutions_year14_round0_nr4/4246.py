#include<cstdio>
#include<set>
using namespace std;

#define MAX 1005

int main()
{
	int t, n;
	double a[MAX], b[MAX];

	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		scanf("%d", &n);
		
		set<double> treea, treeb;
		set<double>::iterator it;
		for(int i=0; i<n; ++i) scanf("%lf", &a[i]), treea.insert(a[i]);
		for(int i=0; i<n; ++i) scanf("%lf", &b[i]), treeb.insert(b[i]);
		
		int win1b = 0;
		for(int i=0; i<n; ++i)
		{
			double wa = *treea.begin(); treea.erase(treea.begin());

			it = treeb.upper_bound(wa);
			if(it == treeb.end()) treeb.erase(treeb.begin());
			else win1b++, treeb.erase(it);
		}
		
		int win2b = 0;
		for(int i=0; i<n; ++i) treea.insert(a[i]), treeb.insert(b[i]);
		for(int i=0; i<n; ++i)
		{
			double wa = *treea.begin(); treea.erase(treea.begin());

			it = treeb.upper_bound(wa);
			if(it != treeb.end())
			{
				if(*treeb.begin() < wa) treeb.erase(treeb.begin());
				else treeb.erase(*treeb.rbegin()), win2b++;
			}
			else treeb.erase(treeb.begin());
		}

		printf("Case #%d: %d %d\n", tc, n-win2b, n-win1b);
	}

	return 0;
}
