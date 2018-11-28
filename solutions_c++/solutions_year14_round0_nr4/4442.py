#include"stdio.h"
#include"algorithm"
using namespace std;
double a[1111],b[1111];
int main(){
	int t,cas=1;
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		scanf("%lf",&a[i]);
		
		for(int i=0;i<n;i++)
		scanf("%lf",&b[i]);
		
		sort(a,a+n);
		sort(b,b+n);
		int s1=0,s2=0;
		int ans2=n;
		while(s1<n&&s2<n)
		{
			if(a[s1]<b[s2])
			{
				ans2--;
				s1++;
				s2++;
			}
			else{
				s2++;	
			}
		} 
		s1=0;
		s2=0;
		int ans1=0;
		while(s1<n&&s2<n)
		{
			
			if(a[s1]>b[s2])
			{
				ans1++;
				s1++;
				s2++;
			}
			else {
				s1++;
			}
		}
		printf("Case #%d: %d %d\n",cas++,ans1,ans2);
	}
}