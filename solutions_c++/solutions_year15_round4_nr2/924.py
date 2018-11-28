#include <bits/stdc++.h>
#define EPS 1e-9

using namespace std;

int n,m;
char M[110][110];
long double water[200][2];

int main(){


	int t,ca = 1;
	scanf("%d",&t);
	while(t--){
		printf("Case #%d: ",ca++);
		int n;
		long double v,x;
		scanf("%d %Lf %Lf",&n,&v,&x);
		for(int i = 0;i<n;i++)
			scanf("%Lf %Lf",&water[i][0],&water[i][1]);

		if(n == 2 && fabs(water[0][1]-water[1][1])<EPS ){
			n = 1;
			water[0][0] = water[0][0]+water[1][0];
		}

		if(n == 2 && fabs(water[0][1]-x)<EPS){
			n = 1;
		}
		if(n == 2 && fabs(water[1][1]-x)<EPS){
			n = 1;
			water[0][0] = water[1][0];
			water[0][1] = water[1][1];
		}

		if(n == 1){
			if((water[0][1]>x ) || (water[0][1]<x)){
				printf("IMPOSSIBLE\n");
				continue;
			}

			printf("%.9Lf\n",v/water[0][0]);
			
			continue;
		}

		if((water[0][1]>x && water[1][1]>x) || (water[0][1]<x && water[1][1]<x)){
			printf("IMPOSSIBLE\n");
			continue;
		}

		if(water[0][1]<water[1][1]){
			swap(water[0][0],water[1][0]);
			swap(water[0][1],water[1][1]);
		}

		long double razao = (x - water[1][1])/(water[0][1] - x);
		
		
		long double v0 = (v*razao)/(razao+1.0);
		long double v1 = (v)/(razao+1.0);
		long double s = max(v0/water[0][0],v1/water[1][0]);
		printf("%.9Lf\n",s);

	}
	return 0;
}