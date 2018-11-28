
#include <cstdio>


typedef long long LL;
const int N = 10000010;

bool isok[N];
int sum[N];


bool test(LL k){
	LL i=k;
	LL j=0;
	while(i){
		j = j*10+(i%10);
		i /= 10;
	}

	return j==k;
}

void init()
{
	for(int i=1; i<N; ++i){
		isok[i] = test(i) && test( (LL)i*(LL)i);
		sum[i] += sum[i-1] + (isok[i]?1:0);
	}
}

int bs(LL k)
{
	LL l=0,r=N;
	while(l<r){
		LL mid = (l+r+1)>>1;
		if( mid*mid <k )
			l = mid;
		else
			r = mid-1;
	}

	return (int)l;
}

int main()
{
	init();

	int t,cs=0;
	scanf("%d",&t);
	while(cs++<t){
		LL a,b;
		scanf("%lld%lld",&a,&b);
		int s = bs(a);
		int t = bs(b+1);

		printf("Case #%d: %d\n", cs, sum[t]-sum[s]);
	}


	return 0;
}

/*

		int i=1;
		while(i*i<a) i++;
		int res = 0;
		while(i*i<=b){
			if(test(i) && test(i*i)){
				res++;	
				//printf("%d -> %d\n",i*i,i);
			}
			i++;
		}


*/
