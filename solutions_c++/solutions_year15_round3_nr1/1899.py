#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define ll long long
using namespace std;

int main(){ _
	int T, R, C, W, i, result;
	scanf("%d", &T);
	for(i=1;i<=T;i++){
	   scanf("%d%d%d", &R, &C, &W);
	   result = R*((C + W - 1)/W) + W - 1;
	   printf("Case #%d: %d\n", i, result);
	}
	return 0;
}
