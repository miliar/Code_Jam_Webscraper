#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
vector<double> a1,a2;
int search(vector<double> & v, double target) {
	int lo = 0;
	int hi = v.size() - 1;
	while(lo < hi) {
		int m = (lo + hi) / 2;
		if(target < v[m]) {
			hi = m;
		} else {
			lo = m + 1;
		}
	}
	if(lo == v.size() - 1 && v[lo] < target) {
		return -1;
	} else {
		return lo;
	}
}
int greedy(vector<double> v1, vector<double> v2) {
	sort(v2.begin(), v2.end());
	int sum = 0;
	for(int i = 0; i < v1.size(); i++)
	{
		double current = v1[i];
		int index = search(v2, current);
		if(index == -1)
		{
			v2.erase(v2.begin());
		} else {
			v2.erase(v2.begin() + index);
			sum ++;
		}
		/*
		for(int i = 0; i < v2.size(); i++)
			printf("%lf ",v2[i]);
		printf("\n");
		*/
	}
	return sum;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int z = 1; z <= t; z++) {
		printf("Case #%d: ", z);
		int n;
		scanf("%d",&n);
		a1.resize(n);
		a2.resize(n);
		for(int i = 0; i < n; i++) {
			scanf("%lf",&a1[i]);
		}
		for(int i = 0; i < n; i++) {
			scanf("%lf",&a2[i]);
		}
		printf("%d %d\n",greedy(a2, a1), n - greedy(a1, a2));
	}
	return 0;
}