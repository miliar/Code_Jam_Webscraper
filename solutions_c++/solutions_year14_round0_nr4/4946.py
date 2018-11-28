#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
	
	int t,i,j,cas=1,n,war,deceit,naml,namr,kenl,kenr,count,f;
	double temp;
	int nam[1010],ken[1010],flag[1010];
	
	scanf("%d",&t);
	
	while(t--){
		war=0;
		deceit=0;
		
		scanf("%d",&n);
		
		for(i=0;i<n;i++){
			scanf("%lf",&temp);
			nam[i]=temp*100000;
			}
			
		for(i=0;i<n;i++){
			scanf("%lf",&temp);
			ken[i]=temp*100000;
			}
		
		sort(nam,nam+n);
		sort(ken,ken+n);
		
		memset(flag,0,sizeof(flag));
		for(i=0;i<n;i++){
			f=0;
			for(j=0;j<n;j++){
				if(ken[j]>nam[i] && !flag[j]){
					f=1;
					flag[j]=1;
					break;}}
				
			if(!f)
				war++;
			}
		
		
		naml=kenl=0;
		namr=kenr=n-1;
		count=0;
		while(count<n)
		{
			if(nam[naml]<ken[kenl]){
				naml++;
				kenr--;}
				
			else{
				naml++;
				kenl++;
				deceit++;
				}
			count++;
		}
		printf("Case #%d: %d %d\n",cas,deceit,war);
		cas++;
	}
	
	return 0;
}
		
		