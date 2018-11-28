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
	for(tt=1; tt<= Test; tt++){
		scanf(" %d",&n);
		int res = 0;
		int cur = 0;
		for(int i = 0 ; i<= n;i++)
		{
			int x;
			char ch;
			scanf(" %c",&ch);
			x = ch - '0';
			if(cur >= i){
				cur += x;
			}
			else{
				res += i - cur;
				cur = i + x;
			}
		}
		printf("Case #%d: %d\n",tt,res);
	}
	return 0;
}
