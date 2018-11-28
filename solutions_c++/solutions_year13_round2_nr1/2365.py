#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <ctime>
#include <memory.h>

using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define ABS(n) ((n)<0 ? -(n) : (n))
#define SQR(a) (a)*(a)
#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define COPY(a,b) memcpy(a,b,sizeof (b));
#define SI(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define SORT(c) sort(ALL(c))
const double PI = 2*acos(0.0);

vector<unsigned long long> arr;

unsigned long long solve2(unsigned long long A, int current, unsigned long long last)
{
	if (current == last)
	{
		return 0;
	}

	if (A > arr[current])
	{
		return solve2(A+arr[current], current + 1, last);
	}
	
	unsigned long long left, right;

	if (1 == A)
	{
		left = ULLONG_MAX / 2;
	}
	else
	{
		left = solve2(2*A - 1, current, last);
	}

	right = solve2(A, current, last - 1);
	return MIN(left, right) + 1;	
}



void SolveCase(int caseIndex)
{
	unsigned long long A, N;
	unsigned long long solve;
	
	
	cin >> A >> N;
	arr.clear();
	for (int i = 0; i < N; i++)
	{
		unsigned long long temp;
		cin >> temp;
		arr.push_back(temp);
	}

	SORT(arr);

	int i = 0;

	while (i < N && arr[i] < A)
	{
		A += arr[i];
		i++;
	}	

	if (i == N)
	{
		solve = 0;
	}
	else
	{
		solve = solve2(A, i, N);
	}
	
	cout << "Case #" << caseIndex + 1 << ": " << solve << endl;
}


void main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;
	
	REP(caseIndex, numCases)
	{
		SolveCase(caseIndex);
	}
}

