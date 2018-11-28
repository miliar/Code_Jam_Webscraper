#include<cstdio>
#include<algorithm>
#include<cmath>
typedef long long i64;

int tc;
i64 R, T;
double PI = 3.1415926535897932384626433;

bool test(i64 cnt)
{
	return R*cnt*2 + cnt*(cnt*2-1) <= T;
}

int main()
{
	scanf("%d", &tc);
	for(int t=0;t++<tc;){
		scanf("%lld%lld", &R, &T);

		i64 ret = 0, width = 1;
		for(;;){
			if(test(width)){
				ret = width;
				width *= 2;
			}else break;
		}

		width /= 2;
		while(width){
			if(test(ret + width)){
				ret += width;
			}
			width /= 2;
		}

		printf("Case #%d: %lld\n", t, ret);
	}

	return 0;
}
