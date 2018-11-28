#include<stdio.h>
#include<algorithm>
using namespace std;
char in[120];
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;scanf("%d%d",&a,&b);
		int f=0;
		bool dame=false;
		for(int i=0;i<a;i++){
			scanf("%s",in);
			bool ok=true;
			for(int j=0;in[j];j++)if(in[j]=='0')ok=false;
			if(ok)dame=true;
		//	if(in[0]=='1')f|=1;
		//	if(in[b-1]=='1')f|=2;
		//	if(in[b-1]=='1'&&in[0]=='1')dame=true;
		}
		scanf("%s",in);
		if(dame){
			printf("Case #%d: IMPOSSIBLE\n",t);continue;
		}
		printf("Case #%d: ",t);
			for(int i=0;i<50;i++)printf("%d",(i+1)%2);
			printf("?");
			for(int i=0;i<50;i++)printf("%d",(i+1)%2);
			printf(" 0");
			for(int i=0;i<b-1;i++)printf("?");
			printf("\n");
	}
}