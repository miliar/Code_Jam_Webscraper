#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
	freopen("D-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int _=1;_<=t;_++){
		printf("Case #%d: ",_);
		int n;
		scanf("%d",&n);
		double arr1[1000],arr2[1000];
		bool b1[1000],b2[1000];
		for(int i=0;i<n;i++)
			scanf("%lf",&arr1[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&arr2[i]);
		for(int i=0;i<n;i++) b1[i]=b2[i]=true;
		sort(arr1,arr1+n);
		sort(arr2,arr2+n);
		//Shaco Q
		int cnt2=0;
		for(int i=0;i<n;i++){
			int min,max;
			for(int j=0;j<n;j++){
				if(b2[j]){
					min=j;
					break;
				}
			}
			for(int j=n-1;j>=0;j--){
				if(b2[j]){
					max=j;
					break;
				}
			}
			if(arr1[i]<arr2[min]){
				b2[max]=false;
			}else{
				b2[min]=false;
				cnt2++;
			}
		}
		printf("%d ",cnt2);
		//war
		int cnt=n;
		for(int i=0;i<n;i++){
			bool flag=true;
			for(int j=0;j<n;j++){
				//printf("%lf %lf\n",arr2[j],arr1[i]);
				if(arr2[j]>arr1[i] && b1[j]){
					b1[j]=false;
					cnt--;
					flag=false;
					break;
				}
			}
			if(flag){
				for(int j=0;j<n;j++){
					if(b1[j]){
						b1[j]=false;
						break;
					}
				}
			}
		}
		printf("%d \n",cnt);
	}
}