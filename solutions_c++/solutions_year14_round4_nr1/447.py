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

const int nmax = 10005;
int a[nmax];

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		int n, x;
		cin >> n >> x;
		for(int i=0;i<n;i++)
			cin >> a[i];
		sort(a, a+n);
		int c = 0;
		for(int i=0,j=n-1; i<=j; )
		{
			c++;
			if(i == j)
				break;
			if(a[i] + a[j] <= x)
			{
				i++;
				j--;
			}
			else
				j--;
		}
		printf("Case #%d: %d\n", test_case, c);
		
	}
	return 0;
}
