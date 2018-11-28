#include <cstdio>
#include <algorithm>
using namespace std;
int main(int argc, char const *argv[])
{
	int  t;
	scanf(" %d",&t);
	int tt=0;
	while(tt<t){
		tt++;
		int n,i;
		scanf(" %d",&n);
		double arr1[1000],arr2[1000];
		for(i=0;i<n;i++){
			scanf(" %lf",&arr1[i]);
		}
		for(i=0;i<n;i++){
			scanf(" %lf",&arr2[i]);
		}
		sort(arr1,arr1+n);
		sort(arr2,arr2+n);
		int p1=0,p2=0;
		int points=0;
		for(p1=0;p1<n;p1++){
			if(arr1[p1]>arr2[p2]){
				p2++;
				points++;
			}

		}
		int points_or=0;
		p2=n-1;
		for(p1=n-1;p1>=0;p1--){
			if(arr1[p1]>arr2[p2]){
				points_or++;
			}
			else{
				p2--;
			}

		}
		printf("Case #%d: %d %d\n",tt,points,points_or);

	}
	
	return 0;
}