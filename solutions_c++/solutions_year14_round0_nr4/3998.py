#include<cstdio>
#include<iostream>
#include<map>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
#include<climits>
using namespace std;

double na1[1005],na2[1005];
double ken1[1005],ken2[1005];
int result1,result2;



int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc,n;
	double target;
	scanf("%d",&tc);
	for(int k=1;k<=tc;k++){
		
		result1 = result2 = 0;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%lf",na1+i);
		}
		for(int i=0;i<n;i++){
			scanf("%lf",ken1+i);
		}
		
		sort(na1,na1+n);
		sort(ken1,ken1+n);
		
		for(int i=0;i<n;i++){
			na2[i]=na1[i];
			ken2[i]=ken1[i];
		}
		
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(ken1[i]<na1[j]){
					result1 += 1;
					na1[j]=INT_MIN;
					break;
				}
				else{
					continue;
				}
			}
		}
		
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(na2[i]<ken2[j]){
					ken2[j]=INT_MIN;
					result2 ++;
					break;
				}
				else{
					continue;
				}
			}
		}
		printf("Case #%d: %d %d\n",k,result1,n-result2);
	}
	return 0;
}
