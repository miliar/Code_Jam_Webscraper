#include <cstdio>

using namespace std;

long i,j,a,b,k,tc;
long long nr;

int main () {
	
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	long lel=0;
	scanf("%ld",&tc);
	while(tc--){
		lel++;
		nr=0;
		scanf("%ld%ld%ld",&a,&b,&k);
		for(i=0;i<a;i++)
			for(j=0;j<b;j++)
			{
				long cij=i&j;
				if(cij<k)
					nr++;
			}
		printf("Case #%ld: %I64d\n",lel,nr);
	}
	return 0;
}
