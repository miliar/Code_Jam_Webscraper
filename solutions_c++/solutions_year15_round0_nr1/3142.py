#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<iomanip>
#include<fstream>
#include<ctime>
using namespace std;
typedef vector<int> VI;
typedef pair <int,int> ii;
typedef long long LL;
#define pb push_back
const int INF = 2147483647;

int z,n,c,i,sum,res,q;
char t[1005];

int main() {
scanf("%d",&z);
for (q=1;q<=z;q++) {
	scanf("%d %s",&n,t);
	sum = 0;
	res = 0;
	for (i=0;i<=n;i++) {
		c = int(t[i] - '0');
		if (c > 0) {
			if (sum < i) {
				res += (i - sum);
				sum = i;
			}
			sum += c;
		}
	}
	printf("Case #%d: %d\n", q, res);
}
return 0;
}

