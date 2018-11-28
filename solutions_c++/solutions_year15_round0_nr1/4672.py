#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
	int T;
	scanf("%i",&T);
	for(int j = 1;j<=T;j++){
		int S,need=0,got=0;
		scanf("%i",&S);
		char people[S+1];
		scanf("%*[ \n\t]");
		for(int i = 0; i<=S;i++){
			char temp;
			scanf("%c",&temp);
			people[i]=temp;
		}
		for(int i = 0; i<=S;i++){
			if(got>=i){
				got += (people[i] - '0');
				continue;
			}
			else{
				need += i-got;
				got += (people[i] - '0') + (i-got);
			}
		}
		printf("Case #%i: %i\n",j,need);
	}
	return 0;
}