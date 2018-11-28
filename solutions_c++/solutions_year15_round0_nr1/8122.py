#include<cstdio>

int main(){
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++){
		int n;
		scanf("%d",&n);
		char s[n+1];
		scanf("%s",s);
		int curr=0,added=0;
		for(int i=0;i<=n;i++){
			int ppl = s[i]-'0';
			if(curr>=n){
				break;
			}else if(i>curr){
				int temp=i-curr;
				added+=temp;
				curr+=ppl+temp;
			}else{
				curr+=ppl;
			}
		}
		printf("Case #%d: %d\n",j,added);
	}
	return 0;
}
