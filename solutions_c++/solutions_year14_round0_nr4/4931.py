#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
		freopen("21.txt","w",stdout);
	int t=0;
	scanf("%d",&t);
	int time=0;
	while(t--){
		int a,b;
		time++;
		scanf("%d",&a);
		double x[a];
		double y[a];
	
		for(int i=0;i<a;i++){
			scanf("%lf",&x[i]);
		}
		//scanf("%d",&b);
		b=a;
		for(int i=0;i<b;i++){
			scanf("%lf",&y[i]);
		}
		sort(x,x+a);
		sort(y,y+b);
		
		int k=b-1;
		int j=0;
		int ans1=0,ans2=0;
		for(int i=a-1;i>=0;i--){
			if(x[i]>y[k]){
				j++;
			}else{
				k--;	
			}
		}
		ans1=j;
		j=0;
		k=b-1;
		for(int i=0;i<a;i++){
		//	printf("%lf %lf\n",x[i],y[j]);
			if(x[i]<y[j] ){
	//			printf("here\n");
				ans2++;
			}else{
				j++;
			}
			
		}
		
		ans2=a-ans2;;
		printf("Case #%d: %d %d\n",time,ans2,ans1);
	//	return 0;
	}
	return 0;
}
