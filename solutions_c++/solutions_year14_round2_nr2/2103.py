#include <stdio.h>

int casos,a,b,k,r;

int main(){
	freopen("in.txt","r",stdin);
	scanf("%d",&casos);
	for(int c = 1;c <= casos;c++){
		scanf("%d %d %d",&a,&b,&k);
		for(int i = 0;i < a;i++)
			for(int j = 0;j<b;j++)
				if((i&j) < k)r++;
		printf("Case #%d: %d\n",c,r);
		r = 0;
	}		
	return 0;
}
