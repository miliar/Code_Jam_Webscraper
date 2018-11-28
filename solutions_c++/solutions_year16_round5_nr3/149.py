#include <bits/stdc++.h>

using namespace std;

int t,tes,i,n,k,j;
double base,top,mid;
double x[1007],y[1007],z[1007],dum[1007];
bool visited[1007];

void DFS(int j) {
	int i;
	for (i=0 ; i<n ; i++) if (!visited[i] && pow(fabs(x[i]-x[j]),2) + pow(fabs(y[i]-y[j]),2) + pow(fabs(z[i]-z[j]),2) <= mid*mid) {
		visited[i] = true;
		DFS(i);
	}
}

int main() {
	scanf("%d",&t);
	for (tes=1; tes<=t ; tes++) {
		scanf("%d%d",&n,&k);
		for (i=0 ; i<n ; i++) {
			scanf("%lf%lf%lf%lf%lf%lf",&x[i],&y[i],&z[i],&dum[i],&dum[i],&dum[i]);
		}
		
		base = 0.0;
		top = 1000000.0;
		
		for (j=0 ; j<200 ; j++) {
			mid = (base + top) / 2.0;
			for (i=0 ; i<n ; i++) visited[i] = false;
			visited[0] = true;
			DFS(0);
			
			if (visited[1]) top = mid; else base = mid;
		}
		
		printf("Case #%d: %.9lf\n",tes,(base+top) / 2.0);
	}
}
