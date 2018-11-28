#include <bits/stdc++.h>

using namespace std;

typedef signed char 		i8;
typedef unsigned char 		i8u;
typedef signed short 		i16;
typedef unsigned short 		i16u;
typedef signed int 			i32;
typedef unsigned int 		i32u;
typedef signed long long 	i64;
typedef unsigned long long 	i64u;

typedef char 				ch;
typedef bool 				bit;

typedef float 				f32;
typedef double 				f64;

typedef vector<i32>			vi;
typedef vector<vi>			vii;
typedef pair<i32, i32> 		pii;





#define DEBUG(n) 		cout << '>' << #n << ": "<< n <<endl;
#define CLEAR(v) 		memset(v, 0, sizeof(v));
#define NEGATE(v) 		memset(v, -1, sizeof(v));
#define FOR(i, n) 		for(i32 i = 0; i < (n); ++i)
#define FORR(i, a, b) 	for(i32 i = (a); i <= (b); ++i)
#define RFOR(i, n) 		for(i32 i = (n - 1); i >= 0; --i)
#define RFORR(i, a, b) 	for(i32 i = (b); i >= (a); --i)
#define ALL(c)			(c).begin(), (c).end()
#define SZ(c)			(i32)((c).size())
#define PB				push_back
#define ITERATE(c, i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define TIME 			cout<< "Time elapsed: "<< clock() / 1000 <<" ms"<<endl;



const i32 MAX = 1e6 + 6;

i32 N;
i32 J;

i64 b_pow[11][16];
i32 divisors[12];

i32 first_div;

bool not_prime(i64 n)
{
	i64 s = sqrt(n);
	FORR(i, 2, s)
	{
		if(n % i == 0)
		{
			first_div = i;
			return 1;
		}
	}

	return 0;
}


void precompute()
{
	FORR(i, 2, 10)
	{
		b_pow[i][0] = 1;
		FORR(j, 1, 15)
			b_pow[i][j] = b_pow[i][j - 1] * i;
	}
}

i64 get_num(i32 b, i32 mask)
{
	i64 n = 0;
	i32 idx = 1;
	while(mask)
	{
		if(mask & 1)
			n += b_pow[b][idx];
		mask >>= 1;
		idx++;
	}

	return n + b_pow[b][N - 1] + 1;
}

i32 main()
{
	precompute();

	i32 T;
	scanf("%d", &T);
	
	i32 C = 0;
	while(T--)
	{
		C++;
		
		scanf("%d %d", &N, &J);
		
		printf("Case #%d:\n", C);
		
		
		i32 limit = 1 << (N - 2);
		i32 counter = 0;
		bool flag;
		i64 n;
		i32 i_c, idx;
		FOR(i, limit)
		{
			if(counter == J)
				break;

			flag = 1;
			FORR(b, 2, 10)
			{
				n = get_num(b, i);
				if(!not_prime(n))
				{
					flag = 0;
					break;
				}
				divisors[b] = first_div;
			}

			if(flag)
			{
				printf("%lld ", n);

				FORR(b, 2, 10)
					printf("%d ", divisors[b]);
				printf("\n");

				counter++;
			}
		}
	}

	return 0;
}