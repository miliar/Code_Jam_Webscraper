#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> vi;
typedef vector<string> vs;
const int INF = 0x7fffffff;

inline bool isPalindrome(lint a)
{
	vi digits;
	while(a != 0)
	{
		digits.push_back(a % 10);
		a /= 10;
	}
	for(int i = 0; i < digits.size() / 2; ++i)
		if(digits[i] != digits[digits.size() - 1 - i])
			return false;
	return true;
}

vector<lint> nums;

lint cnt(lint a)
{
	int l = -1, r = nums.size() - 1;
	while(r - l > 1)
	{
		int x = (r + l) / 2;
		if(nums[x] > a)
			r = x;
		else
			l = x;
	}
	return l + 1;
}

int Solution()
{
	lint a, b;
	cin >> a >> b;
	cout << cnt(b) - cnt(a - 1);
	return 0;
}

#define debug 1

int main()
{
	for(lint i = 1; i <= 10l * 1000 * 1000; ++i)
		if(isPalindrome(i) && isPalindrome(i * i))
			nums.push_back(i * i);

#ifdef debug
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
#endif
	int n;
	cin >> n;
	getchar();
	for(int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		Solution();
		printf("\n");
	}
	return 0;
}
