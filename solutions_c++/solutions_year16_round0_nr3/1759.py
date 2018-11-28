#include <cstdio>
#include <cstdlib>

using namespace std;

int gogo[80]={0};

void doit(){
	gogo[0] = 1;
	gogo[15] = 1;
	gogo[16] = 1;
	gogo[31] = 1;
	for(int x = 0;x < 500;x++){
		for(int y = 0; y < 32; y++) printf("%d",gogo[y]);
		for(long long int j = 2 ; j <=10;j++){
			long long int uccu = 0;
			for(long long int k = 0; k <=15 ;k++){
					uccu*=j;
					if(gogo[k] == 1) uccu++;
			}
			printf(" %lld",uccu);
		}
		printf("\n");
		gogo[14]+=1;
		gogo[30]+=1;
		int r = 14;
		while(gogo[r]>=2){
			gogo[r-1]++;
			gogo[r] = 0;
			r--;
		}
		r = 30;
		while(gogo[r]>=2){
			gogo[r-1]++;
			gogo[r] = 0;
			r--;
		}
	}
	return;
}


main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Output.txt","w",stdout);

	int t,n,j;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&j);
		printf("Case #1:\n");
		doit();
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}