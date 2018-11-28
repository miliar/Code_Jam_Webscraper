#include<iostream>
#include<cstdio>
#define maxn 10000
using namespace std;
int a[maxn];
int main(){
	
	int testCases,Case=1,Max=INT_MIN,totalElements;
	cin>>testCases;
		
	while(testCases--){
	
		scanf("%d",&totalElements);
		Max=INT_MIN;
		
		for(int i=1;i<=totalElements;i++){

			scanf("%d",&a[i]);
			Max=max(Max,a[i]);
		}
		
		int ans=Max;
		for(int i=1;i<=Max;i++){
			
			int temp2=0,temp=0;
			for(int j=1;j<=totalElements;j++){
				
				if(a[j]>i){
					
					temp2 += (a[j] / i)+((a[j]%i==0)?0:1)-1;
					temp=max(temp,i);
				
				}
				
				else temp=max(temp,a[j]);
			
			}
			
			temp2+=temp;
			if(temp2<ans)ans=temp2;
	
		}
	
		printf("Case #%d: %d\n",Case,ans);
	
	}
	
	return 0;

}
