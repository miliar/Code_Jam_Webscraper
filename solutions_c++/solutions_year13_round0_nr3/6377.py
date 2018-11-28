#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include<fstream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
#define rep(x,n) for(int x=0;x<n;++x)
#define rep1(i,s) for(int i = 0; i < (int)s.size(); ++i)
#define mem(a, b) memset(a, b, sizeof(a))

#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define xetBit(code, i) (code & ~(1 << i))
#define PI acos(-1.0)
#define oo (int)10e7
#define rd(x) scanf("%d", &x)
#define rdfile(x) freopen(x, "r", stdin)
#define wtfile(x) freopen(x, "w", stdout)
using namespace std;

#define negmod(x, mod) ((x + mod) % mod)

bool isPalindrome(int num)
{
	int tempNum=num;
	int reversedNum = 0;
	while(tempNum > 9)
	{
		reversedNum += (tempNum % 10);
		reversedNum *=10;
		tempNum /=10;
	}
	reversedNum += tempNum;
	return num == reversedNum;
}
bool Palindrome[1001];
int main()
{
	rdfile("C-small-attempt0.in");
	wtfile("output.txt");
	//isPalindrome(100);
	for(int i=1;i<=1000;++i)
	{
		Palindrome[i]=isPalindrome(i);
	}

	int testcases;
	int A,B;
	int count =0;
	cin>>testcases;
	for(int i=1;i<=testcases;++i)
	{
		cin>>A>>B;
		for(int num=A;num <= B;++num)
		{
			if(!Palindrome[num])
				continue;
			int root = (int)sqrt((double)num);
			if(root*root == num)
			{
				if(Palindrome[root])
					++ count; 
			}
		}
		printf("Case #%d: %d\n",i,count);
		count =0;
	}
	return 0;
}