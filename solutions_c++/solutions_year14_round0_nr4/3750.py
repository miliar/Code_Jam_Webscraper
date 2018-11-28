#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

const int nmax = 1005;
double a[nmax], b[nmax];

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		int n;
		cin >> n;
		for(int i=0;i<n;i++)
			cin >> a[i];
		for(int i=0;i<n;i++)
			cin >> b[i];

		sort(a, a+n);
		sort(b, b+n);
		//for(int i=0;i<n;i++) printf(" %.3f", a[i]); printf("\n");
		//for(int i=0;i<n;i++) printf(" %.3f", b[i]); printf("\n");

		int ptsWar = n;
		for(int i=0, j=0; i<n && j<n; i++, j++)
		{
			while(j<n && a[i] > b[j])
				j++;
			if(j>=n)
				break;
			ptsWar--;
		}
		
		int ptsDeceitful = 0;
		for(int k=0; k<=n; k++)
		{
			bool good = true;
			for(int i=0;i<k;i++)
				if(a[n-k+i] < b[i])
				{
					good = false;
					break;
				}
			if(!good)
				break;
			ptsDeceitful = k;
		}
		
		printf("Case #%d: %d %d\n", test_case, ptsDeceitful, ptsWar);
	}
	return 0;
}
