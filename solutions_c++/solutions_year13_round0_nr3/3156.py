#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <set>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long
#define INF 1000000000

using namespace std;

int T;
LL A, B;
vector<LL> fsnum;

bool isPalindrome(LL num)
{
	char temp[111];
	sprintf(temp, "%I64d", num);
	
	int len = strlen(temp);
	for(int i = 0; 2 * i < len; i++) if(temp[i] != temp[len - i - 1]) return false;
	return true;
}

int main()
{
	for(int i = 1; i <= 1000000; i++) 
		if(isPalindrome((LL) i) && isPalindrome((LL) i * (LL) i))
			fsnum.pb((LL) i * (LL) i);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%I64d %I64d", &A, &B);
		int lower = lower_bound(fsnum.begin(), fsnum.end(), A) - fsnum.begin();
		int upper = upper_bound(fsnum.begin(), fsnum.end(), B) - fsnum.begin();
		printf("Case #%d: %d\n", t, upper - lower);
	}
	return 0;
}

