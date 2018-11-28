#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define VI vector<int>
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define PB push_back

int K,C,S;

LL interpret(int digit,int e,int base){
	//printf("%d * %d ^ %d\n", digit, base, e);
	LL res = 1;
	for(int i=0;i<e;i++)
		res *= base;

	res *= digit;
	return res;
}

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/fractiles_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/fractiles_output2.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);

	for(int t=1;t<=cases;t++){
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d: ", t);
		int R = K/C;
		if(K%C != 0)
			R++;
		if(R > S)
			printf("IMPOSSIBLE\n");
		else{
			//printf("we need %d numbers\n", R);
			for(int i=0;i<R;i++){
				LL idx = 0;
				for(int j=0;j<C;j++){
					idx += interpret(min(i*C+j,K-1),j,K);
				}
				printf("%lld ", idx+1LL);
			}
			printf("\n");
		}
	}
    return 0;
}
