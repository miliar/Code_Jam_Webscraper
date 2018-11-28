#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
	int T,I;
	scanf("%d",&T);
	for(I=0;I<T;I++){
		char s[1500];
		int k,i,j,b[1500];
		scanf("%s %d",s,&k);
		printf("Case #%d: ",I+1);
		int l=strlen(s);
		for(i=0;i<l;i++){
			if(s[i]=='-')b[i]=0;
			else b[i]=1;
		}
		int ans=0;
		for(i=0;i<l;i++){
			if(b[i]==0){
				if(i>l-k)break;
				for(j=0;j<k;j++){
					b[i+j]=(b[i+j]+1)%2;
				}
				ans++;
			}
			//for(j=0;j<l;j++)printf("%d",b[j]);
			//printf("\n");
		}
		if(i==l){
			printf("%d\n",ans);
		}
		else{
			printf("IMPOSSIBLE\n");
		}
	}
}