/*
 * C-Consonants.cpp
 *
 *  Created on: May 12, 2013
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
int const MAX = 102;
int const OO = (1<<28);
char str[MAX];
int N;
bool ch(char x)
{
	return x!='a' && x!='e' && x!='i' && x!='o'&& x!= 'u';
}
int getIndx(int n)
{
	int c=0;
	for(int i=n;str[i];++i)
	{
		if(ch(str[i]))
			c++;
		else
			c=0;
		if(c>=N)
			return i;
	}
	return -1;
}
int main()
{
	freopen("in.in","rt",stdin);
	freopen("out.out","wt",stdout);
	int t,id=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s%d",str,&N);
		int res=0;
		int len = strlen(str);
		for(int i=0;str[i];++i)
		{
			int j = getIndx(i);
			if(j==-1)
				continue;
			res+=(len-j);
		}
		printf("Case #%d: %d\n",id++,res);
	}
}
