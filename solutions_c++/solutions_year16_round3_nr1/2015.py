#pragma warning(disable: 4996)

#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
#include <math.h>
#include <unordered_set>
using namespace std;

#define CURRENT A
#define  A 0 //senator
#define  B 1 //
#define  C 2 //

#if (CURRENT == A)

typedef struct se
{
	int val;
	char  par;
};
//int p[26];
vector<struct se> p;
int np;

void quickSort( int left, int right) 
{
	int i = left, j = right;
	int tmp;
	char tmpP;
	int pivot = p[(left + right) / 2].val;

	/* partition */
	while (i <= j) {
		while (p[i].val < pivot)
			i++;
		while (p[j].val > pivot)
			j--;
		if (i <= j) {
			tmp = p[i].val;
			p[i].val = p[j].val;
			p[j].val = tmp;
			tmpP = p[i].par;
			p[i].par = p[j].par;
			p[j].par = tmpP;
			i++;
			j--;
		}
	};

	/* recursion */
	if (left < j)
		quickSort(left, j);
	if (i < right)
		quickSort( i, right);
}

void solve()
{
	while (p.size()>2)
	{
		int len = p.size();
		quickSort(0, len - 1);
		if ( (p[len-1].val - p[len-2].val) >=2)
		{
			p[len - 1].val -= 2;
			cout << p[len - 1].par << p[len - 1].par << " ";

		}
		else
		{
			if (p[len - 1].val==1)
			{
				cout << p[len - 1].par  << " ";
				p[len - 1].val -= 1;
				p.erase(p.begin() + len - 1);
			}
			else
			{
				cout << p[len - 1].par << p[len - 2].par << " ";
				p[len - 1].val -= 1;
				p[len - 2].val -= 1;
				if (p[len-2].val==0)
				{
					p.erase(p.begin() + len - 2);
				}
			}

		}
	}

	while (p[1].val != p[0].val)
	{
		if (p[1].val > p[0].val)
		{
			cout << p[1].par << " ";
			p[1].val--;
		}
		else
		{
			cout << p[0].par << " ";
			p[0].val--;
		}
	}
	while (p[0].val)
	{
		cout << p[0].par<<p[1].par << " ";
		p[0].val--;
	}
	cout << endl;
}

int main(void)
{
//	freopen("A-small.in", "r", stdin);
	freopen("in.txt", "r", stdin);
	freopen("ALL.out", "w", stdout);
	int nTest;

	//scanf("%d", &nTest);
	p.reserve(26);
	
	cin >> nTest;
	for (int i = 0; i < nTest; i++)
	{
		p.clear();
		cin >> np;
		
		for (int j = 0; j < np; j++)
		{
			struct se tmp;
			cin >> tmp.val;
			tmp.par = 'A' + j;
			p.push_back(tmp);
		}
		cout << "Case #" << i + 1 << ": ";
		solve();
		

	}

	return 1;
}
#endif