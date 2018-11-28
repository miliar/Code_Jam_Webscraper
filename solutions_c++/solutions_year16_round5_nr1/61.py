#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
char in[31000];
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%s",in);
		int n=strlen(in);
		int val=0;
		char now='-';
		int ret=0;
		for(int i=0;i<n;i++){
			if(now==in[i]){
				val--;
				if(val==0)now='-';
				else if(in[i]=='C')now='J';
				else now='C';
				ret+=10;
			}else{
				val++;
				now=in[i];
			}
	//		printf("%d %c\n",val,now);
		}
		ret+=val/2*5;
		printf("Case #%d: %d\n",t,ret);
	}
}