#include <cstdio>
#include <deque>
#include <cstdlib>
#include <limits.h>
#include <algorithm>
#include <set>
using namespace std;
double a1[1001],a2[1001];
multiset<double>s;
multiset<double>::iterator it;
int main()
{
	int t;
	scanf("%d",&t);
	for(int k=0;k<t;k++){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)scanf("%lf",&a1[i]);
		for(int i=0;i<n;i++)scanf("%lf",&a2[i]);
		sort(a1,a1+n);sort(a2,a2+n);
		int qf2=0,ans1=0,ans2=0;
		for(int i=0;i<n;i++){
			double t1=a1[i],t2=a2[qf2];
			if(t1>t2){
				qf2++;
				ans1++;
			}
		}
		s.clear();
		s.insert(1);
		for(int i=0;i<n;i++)s.insert(a2[i]);
		for(int i=0;i<n;i++){
			it=s.upper_bound(a1[i]);
			if(*it==1){ans2++;s.erase(--it);}
			else {s.erase(it);}
		}
		printf("Case #%d: %d %d\n",k+1,ans1,ans2);
	}
	return 0;
}
