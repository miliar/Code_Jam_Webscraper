#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ size()
#define ST begin()
#define ED end()
#define CLR clear()
#define ZERO(x) memset((x),0,sizeof(x))
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
const double EPS = 1e-8;

int T,n;
const int MAX_N = 1111;
char s[MAX_N];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++){
		scanf("%d",&n);
		scanf("%s",s);
		int ans = 0 , sum = 0;
		for(int i=0;i<=n;i++){
			if(sum<i){
				ans += i-sum;
				sum += i-sum;
			}
			sum += s[i]-'0';
		}
		printf("Case #%d: %d\n",cases,ans);
	}
	return 0;
}