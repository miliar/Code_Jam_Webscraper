#include<stdio.h>
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d",&t);
	int s,i,j;
	char a[2000];
	j=1;
	while(t--){
		scanf("%d",&s);
		scanf("%s",a);
		int ans=a[0]-'0',count =0;
		for(i=1;i<=s;i++){
			if(ans<i){
			count+=i-ans;
			ans+=i-ans;
			}
			ans+=a[i]-'0';
		}
		printf("Case #%d: %d\n",j,count);
      j++;
	}
return 0;
}
