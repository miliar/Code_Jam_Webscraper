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

const int max_n = 1005;
int a[max_n];

template<typename T>
int merge_sort_inversions(T a[], int n, T tmp[])
{
	if(n <= 1)
		return 0;

	int mid = n/2;
	int inversions = merge_sort_inversions(a, mid, tmp) + merge_sort_inversions(a + mid, n - mid, tmp);
    
	int i=0, l=0, r=mid;
	while(l < mid && r < n)
		if(a[r] < a[l])
		{
			tmp[i++] = a[r++];
			inversions += mid - l;
		}
		else
			tmp[i++] = a[l++];

	while(r < n)
		tmp[i++] = a[r++];
	while(l < mid)
		tmp[i++] = a[l++];
    
	memcpy(a, tmp, n * sizeof(T));
	return inversions;
}

template<typename T>
int inversions(T a[], int n)
{
	T aa[n];
	memcpy(aa, a, sizeof(T) * n);
	T tmp[n];
	return merge_sort_inversions(aa, n, tmp);
}

int test(int n)
{
	int t[n];
	int best = INF;
	for(int b=0; b<(1<<n); b++)
	{
		for(int i=0;i<n;i++)
			if(b&(1<<i))
				t[i] = a[i];
			else
				t[i] = 2e9 + 5 - a[i];
		int inv = inversions(t, n);
		best = min(best, inv);
	}
	return best;
}

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

		int t = test(n);
		
		printf("Case #%d: %d\n", test_case, t);
		
	}
	return 0;
}
