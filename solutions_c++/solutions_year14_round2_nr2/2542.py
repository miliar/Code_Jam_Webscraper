#include <cstdio>
#include <algorithm>
int main(int argc, char const *argv[])
{
	int t,i;
	scanf(" %d",&t);
	i=0;
	while(i<t){
		i++;

		
		int a,b,k;
		scanf(" %d %d %d",&a,&b,&k);
		int res;
		res=a+b-1;//for 0
		int x=1,y=1;
		for(;x<a;x++){
			for(y=1;y<b;y++){
				if((x&y) < k)
					res++;
			}
		}
		printf("Case #%d: %d\n",i,res);



}
}

	