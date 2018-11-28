#include<iostream>
using namespace std;

int T,R,C,W;


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int rec[22][22];
	int res=0;
	scanf("%d",&T);
	for(int k=1;k<=T;k++){
		scanf("%d%d%d",&R,&C,&W);
		memset(rec,0,sizeof(rec));
		res=0;
		for(int i=0;i<R;i++){
			if(i<R-1){
				res+=C/W;
			}
			else{
				if(C%W==0){
					res+=C/W+W-1;
				}
				else{
					res+=C/W+W;
				}
				
			}
		}
		printf("Case #%d: %d\n",k,res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}