#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

double a[400], b[400];
int n, m;
double ret, rett;

void doit(int o, int remain, double current){
	if (remain==0){
		for (int i=o; i<m; i++)
			current *= b[i];

		ret += current;
		return;
	}

	if (m-o<remain){
		return;
	}

	doit(o+1, remain, current * b[o]);
	doit(o+1, remain-1, current * (1-b[o]));
}

void ch(int o, int remain){
	if (remain==0){
		ret = 0;
		doit(0, m/2, 1);
		if (ret>rett) rett = ret;
		return;
	}

	if (n-o<remain){
		return;
	}

	ch(o+1, remain);
	b[m-remain] = a[o];
	ch(o+1, remain-1);
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("small.out","w",stdout);
	
	int task; scanf("%d", &task);
	for (int cs=1; cs<=task; cs++){
		scanf("%d%d", &n, &m);
		for (int i=0; i<n; i++)
			scanf("%lf", a+i);

		rett = 0;
		ch(0, m);
		printf("Case #%d: %.6lf\n", cs, rett);
	}	

	return 0;
}
