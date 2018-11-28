#include<iostream>
#include<cstdio>
#include<climits>
#include<string>
#include<vector>
#define MAX_L 1e6+1
#define GI ({int t; scanf("%d", &t); t;}) 
#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b)) 
using namespace std;

int main(){

	int t;
	t = GI;

	for(int z = 1; z <= t; z++)
	{
		int D;
		D = GI;

		int res = MAX_L ;
		std::vector<int> v(D);

		int mx = -1;
		for(int i = 0 ; i < D; i++){
			v[i] = GI;
			mx = max(mx, v[i]);
		}

		for (int i = 1; i <= mx; ++i)
		{
			/* code */
			int sp = 0 ;
			for (int j = 0; j < D; ++j)
			{
				/* code */

				if(v[j] > i){
					sp += (v[j]-1)/i;
				}

			}

			res = min(res, sp+i);
		}



		printf("Case #%d: %d\n", z, res);
	}

	return 0;

}