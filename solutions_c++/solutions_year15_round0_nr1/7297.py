#include<iostream>
using namespace std;
#include<stdio.h> 
#include<string.h>

int required_for_stand_up(int n,char *a);
int main(){
	int tc,ans,n,num=1;
	scanf("%d",&tc);
	while(tc--){
		scanf("%d",&n);
		char a[2000];
		scanf("%s",a);
		ans=required_for_stand_up(n,a);
		printf("Case #%d: %d\n",num++,ans);
	}
	return 0;
}
int required_for_stand_up(int n,char *a){
	int buddy=0,ans,i,j,status=0;
	ans=a[0]-'0';
	for(i=1 ; i<=n ; i++){
		if(ans<i){
			buddy++;
			status=1;
		}
		else
		status=0;
		ans=ans+a[i]-'0'+status;
	}
	return buddy;
}
