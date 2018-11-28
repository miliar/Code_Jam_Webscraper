#include "cstdio"
int main()
{
	freopen("D-small-attempt0.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,k,c,s;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d %d %d",&k,&c,&s);
		if(k == 1){
			printf("Case #%d: 1\n", i+1);
		}
		else{
			if(c==1){
				if(k==s){
					printf("Case #%d:", i+1);
					for(int j=0;j<s;j++){
						printf(" %d", j+1);
					}
					printf("\n");
				}
				else{
					printf("Case #%d: IMPOSSIBLE\n", i+1);
				}
			}
			else{
				if(s>=k-1){
					printf("Case #%d:",i+1 );
					for(int j=0;j<k-1;j++){
						printf(" %d",2+j*(k+1));
					}
					printf("\n");
				}
				else{
					printf("Case #%d: IMPOSSIBLE\n", i+1);
				}
			}
		}
	}
	return 0;
}