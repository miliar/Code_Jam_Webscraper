#include<cstdio>

bool ans[1024];

inline bool check_pali( int nr )
{
	static int nr_1, rev;
	
	nr_1 = nr; rev = 0;
	
	while( nr_1 > 0 )
	{
		rev = rev * 10 + nr_1 % 10;
		nr_1 /= 10;
	}
	
	return rev == nr;
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);

	for( int i = 1; i * i <= 1000; ++i ){
		ans[i*i] = check_pali(i) && check_pali(i*i);		
	}
	
	int T;
	
	scanf("%d",&T);
	
	int k = 1;
	while( T-- )
	{
		printf("Case #%d: ",k++);
		
		int A, B;
		scanf("%d %d\n",&A,&B);
	
		int counter = 0;
		for(int i = A; i <= B; ++i ){	
			if( ans[i] ) ++counter;		
		}
		
		printf("%d\n",counter);
	}
}
