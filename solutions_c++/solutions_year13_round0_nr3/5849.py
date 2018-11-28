#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <climits>
#include <queue>

using namespace std;

const double Pi=acos(-1.0);
const double Eps=1e-8;

bool isPalindrome(int n)
{
	ostringstream oss;
	oss << n;
	string str = oss.str(), revstr = str;
	reverse(revstr.begin(), revstr.end());
	return str == revstr;	
}

int int_sqrt(int n)
{
	double root = sqrt(double(n));
	return int(root+0.5);
}

bool isFairAndSquare(int n)
{
	int int_root = int_sqrt(n);
	return isPalindrome(n) && int_root*int_root == n && isPalindrome(int_root);
}


int main()
{
	clock_t start = clock();
	int T;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for(int test = 0; test<T; ++test)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		int count  = 0;
		for(int i = a; i<=b; ++i)
			if(isFairAndSquare(i))
				++count;
		printf("Case #%d: %d\n", test+1, count);
	}
	fprintf(stderr, "Time elapsed: %.4lf\n", (double(clock())-start)/CLOCKS_PER_SEC);
	return 0;
}
