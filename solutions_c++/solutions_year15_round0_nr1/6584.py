#include<cstdio>
int s;
char ch[1003];
int su[1003];
int main(){
	int t,turn,i,cnt=0,dap;
	scanf("%d",&turn);
	for(t=1;t<=turn;t++){
		scanf("%d",&s);
		scanf("%s",ch);
		for(i=0;i<=s;i++){
			su[i]=ch[i]-48;
		}
		cnt=su[0];
		dap=0;
		for(i=1;i<=s;i++){
			if(cnt<i){
				dap++;
				cnt++;
			}
			cnt+=su[i];
		}
		printf("Case #%d: %d\n",t,dap);
	}
}