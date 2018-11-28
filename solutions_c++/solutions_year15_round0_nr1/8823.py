#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <cmath>
#include <stack>
#include<math.h>
#include<string.h>
using namespace std;
#define MOD 1000000007
#define MAX 100000
#define INF 0x3fffffff
#define LL long long
#define LLU unsigned long long
#define PII pair<int,int>
#define MP(x,y) make_pair(x,y)
#define CLR(x) memset(x,0,sizeof(x))
#define S(x) scanf("%d",&x)
#define SL(x) scanf("%lld",&x)
#define PR(x) printf("%d\n",x)
#define PRL(x) printf("%lld\n",x)

int main() {
	int t;
	S(t);
	for(int test=0;test<t;test++) {

		int n,cnt=0;
		scanf("%d ",&n);
		char ch;
		int totalCnt = 0;
		for(int i=0;i<=n;i++) {
			scanf("%c",&ch);
			int num = (ch-'0');
			if(i!=0 && totalCnt<i) {
				cnt++;
				totalCnt++;
			}
			totalCnt+=num;
		}
		printf("Case #%d: %d\n",test+1,cnt);
	}
	return 0;
}


