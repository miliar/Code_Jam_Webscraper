#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long lint;

vector<lint> pal;

bool isPalin(lint x)
{
	int left = 0, right;
	char str[32];
	right = sprintf(str, "%lld", x) - 1;
	
	while (left < right){
		if (str[left++] != str[right--]) return (false);
	}
	return (true);
}

int main()
{
	
	for (int i = 1; i <= 1000000; i++){
		if (isPalin(i) && isPalin((lint)i * i)) pal.push_back((lint)i * i);
	}
	
	int T;
	
	scanf("%d", &T);
	
	for (int testcase = 1; testcase <= T; testcase++){
		int A, B;
		scanf("%d %d", &A, &B);
		printf("Case #%d: %d\n", testcase, upper_bound(pal.begin(), pal.end(), B) - upper_bound(pal.begin(), pal.end(), A - 1));
	}
	
	return (0);
}
