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



bool digit[11];


i32 main()
{
	i32 T;
	scanf("%d", &T);
	
	i32 N;
	i32 C  = 0;
	while(T--)
	{
		C++;
		CLEAR(digit);
		scanf("%d", &N);

		printf("Case #%d: ", C);
		if(N == 0)
			printf("INSOMNIA\n");
		else
		{
			i64 sum = N;
			i32 r;
			i32 counter = 0;
			i64 sum_c;
			while(1)
			{
				sum_c = sum;
				while(sum_c)
				{
					r = sum_c % 10;
					if(!digit[r])
					{
						digit[r] = 1;
						counter++;
					}

					sum_c /= 10;
				}

				if(counter == 10)
					break;
				sum += N;
			}

			printf("%lld\n", sum);
		}
	}


	return 0;
}