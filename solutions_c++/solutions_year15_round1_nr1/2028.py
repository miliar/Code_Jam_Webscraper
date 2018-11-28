#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#define GI ({int t; scanf("%d", &t); t;}) 
#define max( a , b ) ((a) > (b) ? (a) : (b) )
#define min( a , b ) ((a) < (b) ? (a) : (b) )
using namespace std;

int main(){

	int t;
	t = GI;

	for(int z = 1; z <= t; z++)
	{
		int mx = 0;
		int N = GI;
		int x = GI;
		long int res1, res2;
		res1 = res2 = 0;
		std::vector<int> v(N);
		v[0] = x;
		for(int i = 1 ; i < N; i++){
			int y = GI;
			v[i] = y;
			if(x-y > 0){
				res1 += x - y;
				mx = max(mx, x - y);
			}
			x = y;
		}

		for(int i = 0 ; i < N - 1; i++){
			res2 += min(v[i], mx);
		}
		printf("Case #%d: %ld %ld\n", z, res1, res2);
	}

	return 0;

}