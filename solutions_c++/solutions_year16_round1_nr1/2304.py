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


const i32 MAX = 1000 + 5;
ch str[MAX];
ch ans[MAX << 1];

i32 main()
{
	i32 T;
	scanf("%d", &T);

	i32 C = 0;
	while(T--)
	{
		C++;

		scanf("%s", str);
		i32 len = strlen(str);

		i32 l = 1000, r = 1000;
		FOR(i, len)
		{
			if(i == 0)
			{
				ans[l] = str[i];
				l--;
				r++;
			}
			else
			{
				if(str[i] > ans[l + 1])
					ans[l--] = str[i];
				else if(str[i] < ans[l + 1])
					ans[r++] = str[i];
				else
				{
					i32 s = l + 1;
					while(s < r - 1 && str[s] == str[s + 1])
						s++;
					if(s == r - 1 || str[s] > str[s + 1])
						ans[l--] = str[i];
					else
						ans[r++] = str[i];
				}
			}
		}

		printf("Case #%d: %s\n", C, ans + l + 1);
		CLEAR(ans);
	}


	return 0;
}