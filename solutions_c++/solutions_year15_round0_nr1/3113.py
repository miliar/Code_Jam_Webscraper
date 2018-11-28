#include<cstdio>
int s;
char ch[1003];
int aud[1003];
int main(){
	int t,tc,i,cnt=0,ans;
	scanf("%d",&tc);
	for(t=1;t<=tc;t++){
		scanf("%d",&s);
		scanf("%s",ch);
		for(i=0;i<=s;i++){
			aud[i]=ch[i]-48;
		}
		cnt=aud[0];
		ans=0;
		//printf("%d %d\n",s,su[0]);
		for(i=1;i<=s;i++){
			if(cnt<i){
				ans++;
				cnt++;
			}
			cnt+=aud[i];
		}
		printf("Case #%d: %d\n",t,ans);
	}
}
