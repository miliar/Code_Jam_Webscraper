#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#define mk make_pair
#define lb lower_bound
using namespace std;

double p[212];
double pt[212][212];


int main(){
	int testes,n,k;
	scanf("%d",&testes);
	for(int t=1;t<=testes;t++){
		scanf("%d %d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%lf",&p[i]);
		}
		printf("Case #%d: ",t);
		sort(p,p+n);
		double resp=0.0;
		for(int m=0;m<=k;m++){
			for(int i=0;i<212;i++){
				for(int j=0;j<212;j++){
					pt[i][j]=0.0;
				}
			}
			pt[106][0]=1.0;
			for(int i=0;i<m;i++){
				for(int j=1;j<211;j++){
					pt[j][i+1]=pt[j-1][i]*p[i]+pt[j+1][i]*(1.0-p[i]);
				}
			}
			for(int i=0;i<k-m;i++){
				for(int j=1;j<211;j++){
					pt[j][m+i+1]=pt[j-1][m+i]*p[n-1-i]+pt[j+1][m+i]*(1.0-p[n-1-i]);
				}
			}
			resp=max(resp,pt[106][k]);
		}
		printf("%lf\n",resp);
	}
	return 0;
}
