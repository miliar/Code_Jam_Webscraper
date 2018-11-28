#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#define Rep(i,a) for(int i = 0; i < (a); i++)
#define rep(i,a,b) for(int i = (a); i <= (b); i++)//(a)!
#define dep(i,a,b) for(int i = (a); i >= (b); i--)
#define ab(a) ((a) > 0 ? (a) : -(a))
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back(a)
using namespace std;
typedef long long LL;
typedef unsigned long long uLL;
const int N = 1010;
char s[N];
int f[2];
void work(){
	scanf("%s",s + 1); int n = strlen(s + 1);
	f[0] = f[1] = 0;
	rep(i,1,n){
		if (s[i] == '-') f[1] = f[0] + 1;
		else f[0] = f[1] + 1;
	}
	printf("%d\n",f[1]);
}
int main(){
	int T; scanf("%d",&T);
	int t = 0;
	while (T--) {
		t++;
		printf("Case #%d: ",t);
		work();
	}
	return 0;
}