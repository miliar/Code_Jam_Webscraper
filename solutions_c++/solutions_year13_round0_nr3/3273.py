/*
 * Q-Fair-and-Square.cpp
 *
 *  Created on: Apr 13, 2013
 *  Author: mohamedgamal
 *  Tags:
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <queue>
using namespace std;
#define mp(X,Y) make_pair((X),(Y))
#define SZ(X) (int)((X).size())
typedef pair<int,int> pii;
int const MAX = 0;
int const OO = (1<<28);
bool isPalin(int n)
{
	stringstream ss;
	ss<<n;
	string s;
	ss>>s;
	for(int i=0;i<SZ(s)/2;++i)
		if(s[i]!=s[SZ(s)-i-1])
			return false;
	return true;
}
int main()
{
	freopen("in.in","rt",stdin);
		freopen("out.out","wt",stdout);
	int t,A,B,id=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&A,&B);
		int a = sqrt(A);
		int b = sqrt(B)+1;
		int cnt=0;
		for(int i=a; i<=b;++i)
		{
			if(i*i >= A && i*i <=B)
			{
				if(isPalin(i) && isPalin(i*i))
					cnt++;
			}
		}
		printf("Case #%d: %d\n",id++,cnt);
	}
}
