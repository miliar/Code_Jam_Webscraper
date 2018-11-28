#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 1010
int d[maxn],n;

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		scanf("%d",&n);
		for(int i=1;i<=n;i++){
			scanf("%d",&d[i]);
		}
		int res=100,sum;
		for(int i=1;i<=1000;i++){
			sum=i;
			for(int j=1;j<=n;j++){
				sum+=(d[j]-1)/i;
			}
			res=min(res,sum);
			
		}		
		printf("Case #%d: %d\n", cas, res);
	}
}
	
