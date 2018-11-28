#include<stdio.h>
#include<string.h> 
#include<algorithm>
using namespace std;
int main(){
	

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   
	int t;
	
	scanf("%d",&t);
	
	int cases = 1;
	
	while(t--){
		
		int n;
		scanf("%d",&n);
		
		int s = 0,s1 = 0;
		
		int cha = -1;
		
		int a[10010];
		a[0] = -1; 
		for(int i = 1;i<=n;i++){
			scanf("%d",&a[i]);
			if(a[i] < a[i-1])s+=a[i-1] - a[i];
			
			cha = max(cha,a[i-1] - a[i]);
			
		}
		
		for(int i = 1;i<n;i++){
			
			if(a[i] < cha)s1+=a[i];
			else if(a[i] >= cha) s1 += cha;
			
		}
		
		printf("Case #%d: %d %d\n",cases++,s,s1);
		
	}
	
}