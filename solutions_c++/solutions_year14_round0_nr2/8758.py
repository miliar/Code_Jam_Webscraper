#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

double c, f, x;
double cost(int n){
	double ans = 0;
	for(int i=0; i<n; i++){
		ans += c/(2+(double)i*f);
	}
	ans += x/(2+(double)n*f);
	return ans;
}

int main(){
	double ans;
	int ncases, low, high, mid;
	scanf("%d",&ncases);
	for(int nc=1; nc<=ncases; nc++){
		scanf("%lf %lf %lf",&c,&f,&x);
		low = 0; high = 1000001;
		while(low<high){
			//printf("low %d\n",low);
			//printf("high %d\n",high);
			mid = (low+high)/2;
			
			if(cost(mid)<cost(mid-1) && cost(mid)<cost(mid+1))
				break;

			if(cost(mid-1)>cost(mid+1)){
				low = mid+1;
				//printf("1\n");
			}else if(cost(mid+1)>cost(mid-1)){
				high = mid;
			}
		}
		printf("Case #%d: %.07lf\n",nc,cost(mid));
		//printf("N %d\n",mid);
	}
	return 0;
}
