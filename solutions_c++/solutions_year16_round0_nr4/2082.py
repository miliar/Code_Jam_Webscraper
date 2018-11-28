#include <cstdio>
#include <cstdlib>

main(){
	int t;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("Output.txt","w",stdout);

	scanf("%d",&t);
	for(int z = 1 ;z <= t; z++){
		int a,b,c;
		scanf("%d %d %d",&a,&b,&c);
		printf("Case #%d:",z);
		for(int l = 1;l<=c;l++) printf(" %d",l);
		printf("\n");
	}

	fclose (stdin);
	fclose (stdout);
	return 0;
}