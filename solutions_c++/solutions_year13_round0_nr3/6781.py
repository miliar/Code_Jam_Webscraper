#include <cstdio>
#include <cmath>

bool palin(int x){
	int n = x, r, s=0;
	while(n!=0){
		r = n%10;
		s = s*10+r;
		n/=10;
	}
	return s==x;
}

int main(){
	int t;
	int a, b, i, sroot, count, caseno;
	scanf("%d",&t);
	caseno = 1;
	while(t--)
	{
		scanf("%d%d",&a,&b);
		i = a;
		count = 0;
		while(i<=b)
		{
			if(palin(i))
			{
				sroot = sqrt(i);
				if(sroot*sroot == i && palin(sroot))
				{
					count++;
				}
			}
			i++;
		}
		printf("Case #%d: %d\n",caseno,count);
		caseno++;
	}
}
