#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cstdlib>
#include <cmath>

typedef long long ll;

using namespace std;

#define rep(a,b,c) for(int a=b;a<=c;a++)
#define per(a,b,c) for(int a=b;a>=c;a--)
#define X first
#define Y second
#define PII pair<int,int>
#define pb push_back
#define mp make_pair

const int inf= ~0u>> 1;
int T, N, M, caseCnt, a[111][111], found;

int main(){
	scanf("%d", &T);
	while(T --){
		scanf("%d%d", &N, &M);
		for(int i= 1;i<= N;++ i)
			for(int j= 1;j<= M;++ j)
				scanf("%d", a[i] + j);
		found = 0;
		for(int i= 1;i<= N;++ i)
			for(int j= 1;j<= M;++ j){
				int _max1(-inf), _max2(-inf);
				for(int k= 1;k<= M;++ k)
					_max1= max(_max1, a[i][k]);
				for(int k= 1;k<= N;++ k)
					_max2= max(_max2, a[k][j]);
				if(a[i][j] != _max1 && a[i][j] != _max2){
					found = 1;
//					printf("!:%d %d\n", i, j);
				}
			}
		printf("Case #%d: ", ++ caseCnt);
		puts(found ? "NO" : "YES");
	}
	return 0;
}


