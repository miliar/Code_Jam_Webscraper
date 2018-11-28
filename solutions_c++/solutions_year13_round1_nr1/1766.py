#include <cstdio>

using namespace std;




int main()
{
	int T;
	unsigned long long r,vol;
	unsigned long long no_rings,vol_needed,vol_rem;

	unsigned long long i;
	int k;

	scanf("%d\n",&T);
	
	for(k=0;k<T;k++)
	{
		scanf("%llu %llu\n", &r, &vol);
		vol_rem = vol ;
		no_rings = 0 ;
		
		for(i = r+1; ; i=i+2)
		{
			vol_needed = i<<1;
			vol_needed--;
			if(vol_needed <= vol_rem)
			{
				no_rings++;
				vol_rem -= vol_needed;
			}
			else
				break;
		}
		

		printf("Case #%d: ",k+1);
		printf("%llu\n",no_rings);
	}
}