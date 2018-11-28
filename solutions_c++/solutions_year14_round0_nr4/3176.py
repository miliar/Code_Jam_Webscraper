#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int cmp(int a,int b){
	return a>b;
}

int main(){
	freopen("E:\\C\\D-large.in","r",stdin);
//	freopen("E:\\C\\d.txt","w",stdout);
	int t,cc;
	scanf("%d",&t);

	int weight[2][1100];
	int n;
	int i,j;
	int tmp;
	for(cc=1;cc<=t;cc++){
		getchar();
		int naomi=0,naomi2=0;
		scanf("%d",&n);
		
		for(i=0;i<2;i++){
			getchar();
			for(j=0;j<n;j++){
				if(j==n-1)
					scanf("0.%d",&tmp);
				else
					scanf("0.%d ",&tmp);
		/*		int test=tmp;
				int tt=1;
				int k=1;
				while(test/10>0){
					k++;
					test/=10;
				}
				k=5-k;
				while(k-->0)
					tt*=10;
				tmp*=tt;
		*/
				weight[i][j]=tmp;
			}
		}
		sort(weight[0],weight[0]+n,cmp);
		sort(weight[1],weight[1]+n,cmp);
		int size=n;
		i=j=0;
		while(size>0){
			if(weight[0][i]>weight[1][j]){
				naomi++;
				i++;
			}
			size--;
			j++;
		}
		i=j=n-1;
		
		while(j>=0){
			if(weight[0][i]>weight[1][j]){
				j--;
				naomi2++;
			}else{
				i--;
				j--;
			}
		}
		printf("Case #%d: %d %d\n",cc,naomi,naomi2);

	}

	return 0;
}