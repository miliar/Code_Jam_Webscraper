#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;
int main(int argc, char const *argv[])
{
	int t;
	scanf(" %d",&t);
	int i=0;
	
	while(i<t){
		i++;
		int p,q;
		scanf("%d / %d",&p,&q);
		

		if((q-1)&q){
			printf("Case #%d: impossible\n",i );
			continue;
		}
		double pow=ceil(log2((double)q/(double)p));
		if(pow>40)
			printf("Case #%d: impossible",i);
		else
		printf("Case #%d: %d\n",i,(int)pow);
	}
}
