#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
char find[2000];
int zero,one;

main(){

	freopen("B-large.in","r",stdin);
	freopen("Output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for(int z=1; z<=t ;z++){
		zero = 0;
		one = 0;
		scanf("%s",find);
		int length = strlen(find);
		for(int  k = 1 ; k < length;k++){
			if(find[k] != find[k-1]){
				if(find[k]=='+') one++;
				else zero++;
			}
		}
		if(find[0]=='+') one++;
		else zero++;
		if(find[length-1] == '+') one--;
		if(find[0]=='+') printf("Case #%d: %d\n",z,one + zero);
		else printf("Case #%d: %d\n",z,one + zero);
	}
	
	fclose (stdin);
	fclose (stdout);

	return 0;
}