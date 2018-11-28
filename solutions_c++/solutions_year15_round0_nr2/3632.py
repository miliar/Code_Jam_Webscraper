#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define pb push_back

using namespace std;

const int MAXN = 100010;
const int INF  = 1000000010;
const int mod  = 1000003;

typedef long long Lint;
typedef pair <int,int> pii;

int n,r;
int ar[MAXN];

int main()
{
	int Test,tt;
	scanf(" %d",&Test);
	for(tt = 1 ;tt <= Test ; tt++){
		printf("Case #%d: ",tt);
		scanf(" %d",&n);
		int res = INF;
		for(int i = 1 ; i <= n ;i++) scanf(" %d",&ar[i]);
		for(int i = 1 ; i <= 1000 ;i++){
			int kk = 0;
			int mx = 0;
			for(int j = 1 ; j <= n ;j++){
				int cnt;
				cnt = (ar[j]-1) / i;
				kk += cnt;
			}
			res = min(res,kk+i);

		}
		printf("%d\n", res);
	}
	return 0;
}
