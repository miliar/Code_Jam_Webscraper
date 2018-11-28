#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solveA( int n, vector< int>& arrs)
{
	int ret = 0;
	for( int i=1; i<n; ++i)
	{
		int tmp = arrs[i-1]-arrs[i];
		ret += (tmp>0?tmp:0);
	}
	return ret;
}

int solveB( int n, vector< int> &arrs)
{
	//find max eat speed
	int maxSpeed = 0;
	for( int i=1; i<n; ++i)
	{
		int tmp = arrs[i-1]-arrs[i];
		tmp = tmp>0?tmp:0;
		if(maxSpeed < tmp)
		{
			maxSpeed = tmp;
		}
	}

	int ret = 0;
	for( int i=0; i<n-1; ++i)
	{
		if( arrs[i]<maxSpeed)
			ret += arrs[i];
		else
			ret += maxSpeed;
	}
	return ret;

}


int main()
{
	freopen("A-large.in", "r", stdin);
	int N;
	cin >> N;

	FILE * p; p = fopen ("result.txt","w"); 

	for (int i = 0; i < N; ++i)
	{
		int n;
		cin>>n;
		vector< int> arrs( n, 0);
		for( int i=0; i<n; ++i)
		{
			cin>>arrs[i];
		}
		int retA = solveA( n, arrs);
		int retB = solveB( n, arrs);
		fprintf(p, "Case #%d: %d %d\n", i+1, retA, retB);
	}
	fclose(p);
	return 0;
}
