#include <iostream>
#include <algorithm>

using namespace std;

int YES;
int map[111][111];
int main(){
	long cc,tt;
	long i,j,n,m;
	int big;
	int ans,ans2;
	scanf("%d",&tt);

	for(cc=0;cc<tt;cc++){
		scanf("%d%d",&n,&m);
		YES=1;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&map[i][j]);
		
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++){
				big=0;
				for(int k=0;k<n;k++)
					if(map[i][j]<map[k][j]){
						big++;break;
					}
				for(int k=0;k<m;k++)
					if(map[i][j]<map[i][k]){
						big++;break;
					}
				if(big==2)
					YES=0;
			}

		if(YES)
			printf("Case #%d: YES\n",cc+1);
		else
			printf("Case #%d: NO\n",cc+1);
	}
	return 0;
}