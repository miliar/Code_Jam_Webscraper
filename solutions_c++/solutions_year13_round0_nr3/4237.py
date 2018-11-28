/*
ID: piotrso1
PROG: temp
LANG: C++
*/

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <math.h>

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

long long int arr [39] = { 1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

bool isPal(long long int x)
{
	int i = 0;
	int arr[1000];
	do
	{
		arr[i++] = (int)(x % 10LL);

	}
	while(x /= 10LL);

	int nm = i;

	for(int i = 0; i < nm / 2; i++){
		if(arr[i] != arr[nm - i - 1])
			return false;
	}
  	return true;
}

long long int find_solution(long long int from, long long int to)
{
	long long int to_sqrt = (long long int)sqrt(double(to)) + 1LL;
	long long int res = 0;
	REP(i, to_sqrt)
	{
		if(isPal((long long int)i))
		{
			long long int r = (long long int)i * (long long int)i;
			if(r >= from && r <= to)
			{
				bool isPal_ = (long long int)isPal(r);
				if(isPal_)
					cout<<r<<endl;
				res += (long long int)isPal_;
			}
		}

	}
	return res;
}


void solve(int c, FILE * fin, FILE * fout)
{
	string res;
	long long int A, B;
	fscanf(fin, "%lld %lld", &A, &B);
	int cnt = 0;
	REP(i, 39)
	{
		if(arr[i] >= A && arr[i] <= B)
			cnt++;
	}
	fprintf(fout, "Case #%d: %d\n", c + 1, cnt);

}

int main() {
    	
	FILE *fin, *fout;
    
	fin = fopen("temp.in", "r");
	fout = fopen("temp.out", "w");
	
	int cases;
	fscanf(fin, "%d", &cases);
	REP(i, cases)
	{
		solve(i, fin, fout);
	}

	fclose(fin);
	fclose(fout);
	
	return 0;
}
