#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
int A[2005];
int B[2005];
int TA[2005];
int TB[2005];
vector<int> X;
bool taken[2005];
vector<int> smallerThan[2005];
vector<int> biggerThan[2005];
int n;

bool check()
{
	X.push_back(0);
	TA[0] = 0;
	for(int i = 1;i<=n;i++)
	{
		TA[i] = 0;
		for(int j = 0;j<i;j++)
			if(X[j] < X[i])
				TA[i] = max(TA[i], TA[j] + 1);
		if(TA[i] != A[i])
		{
			X.pop_back();
			return false; 
		}
	}
	TB[n+1] = 0;
	for(int i = n;i>=1;i--)
	{
		TB[i] = 0;
		for(int j = i+1;j<=n+1;j++)
			if(X[i] > X[j])
				TB[i] = max(TB[i], TB[j] + 1);
		if(TB[i] != B[i])
		{
			X.pop_back();
			return false;
		}
	}
	X.pop_back();
	return true;
}
bool backtrack(int depth)
{
	if(depth == n+1)
		return check();
	for(int i = smallerThan[depth].size() + 1;i<=n-biggerThan[depth].size();i++)
		if(!taken[i])
		{
			X.push_back(i);
			taken[i] = true;
			if(backtrack(depth+1))
				return true;
			X.pop_back();
			taken[i] = false;
		}
	return false;
}
void read()
{
	scanf("%d", &n);
	for(int i = 1;i<=n;i++)
		scanf("%d", &A[i]);
	for(int i = 1;i<=n;i++)
		scanf("%d", &B[i]);
	for(int i = 1;i<=n;i++)
	{
		biggerThan[i].clear();
		smallerThan[i].clear();
	}
	X.clear();
	X.push_back(0);
	for(int i = 1;i<=n;i++)
		for(int j = i+1;j<=n;j++)
		{
			if(A[j] <= A[i])
			{
				biggerThan[j].push_back(i);
				smallerThan[i].push_back(j);
			}
			if(B[i] <= B[j])
			{
				
				biggerThan[i].push_back(j);
				smallerThan[j].push_back(i);
			}
		}
	for(int i = 1;i<=n;i++)
	{
		sort(biggerThan[i].begin(), biggerThan[i].end());
		sort(smallerThan[i].begin(), smallerThan[i].end());
		biggerThan[i].erase(unique(biggerThan[i].begin(), biggerThan[i].end()), biggerThan[i].end());
		smallerThan[i].erase(unique(smallerThan[i].begin(), smallerThan[i].end()), smallerThan[i].end());
	}
	for(int i = 1;i<=n;i++)
		taken[i] = false;
}
void solve(int tc)
{
	backtrack(1);
	printf("Case #%d: ", tc);
	for(int i = 1;i<=n;i++)
		printf("%d ", X[i]);
	printf("\n");
}
int main()
{
	int Z;
	scanf("%d", &Z);
	for(int i = 1;i<=Z;i++)
	{
		read();
		solve(i);
	}
	return 0;
}
