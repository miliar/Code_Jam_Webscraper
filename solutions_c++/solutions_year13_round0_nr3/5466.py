#include <cstdlib>
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

int T;
int A, B;
char s[101];
const int MAXN = 1000;
bool fs[MAXN+1];

#define lowbit(a) ((a)&(~(a)+1))
#define N 1000
int C[N];
void modify(int p,int delta)
{
	while (p<=N)
	{
		C[p]+=delta;
		p+=lowbit(p);
	}
}
int sum(int p)
{
	int rs=0;
	while (p)
	{
		rs+=C[p];
		p-=lowbit(p);
	}
	return rs;
}

bool ispalindrome(int n) {
	sprintf(s, "%d", n);
	int len = strlen(s);
	for (int i = 0; i < (len+1)/2; ++i) {
		if (s[i] != s[len-1-i])
			return false;
	}
	return true;
}

int main()
{
	cin >> T;
	for (int i = 1; i*i <= MAXN; ++i) {
		if(ispalindrome(i) && ispalindrome(i*i)) {
			modify(i*i, 1);
		}
	}
	for (int c = 1; c <= T; ++c) {
		cin >> A >> B;

		cout << "Case #" << c << ": ";
		cout << sum(B) - sum(A-1);
		cout << endl;
	}
	return 0;
}
