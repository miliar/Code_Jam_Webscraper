// K1
// :)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <string>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>

#define EPS 1e-8
#define PI 3.141592653589793
#define X first
#define Y second
#define FX(x) fixed << setprecision((x))

using namespace std;

typedef pair<int, int> point;
typedef set<int>::iterator ITR;
const long long MAXN = 1e7 + 1;

long long arr[MAXN];

int rev(int n)
{
	int result = 0;
	while(n)
	{
		(result *= 10 ) += n % 10;
		n /= 10;
	}
	return result;
}

int f(int n)
{
	// cerr << "calc : " << n << endl;
	if(!n) return arr[n] = 0;
	if(arr[n]) return arr[n];
	arr[n] = n;
	if(rev(rev(n)) != n) return arr[n] = f(n-1) + 1;
	// return arr[n] = f(rev(n)) + 1;
	arr[n] = min(f(n-1) + 1, f(rev(n)) + 1);
	return arr[n];
}

int main()
{
	cerr << "start" << endl;
	for (long long i = 0; i < MAXN; ++i)
		arr[i] = MAXN;
	cerr << "init" << endl;
	for (long long i = 0; i < MAXN; ++i){
		if(arr[i] > i) arr[i] = i;
		if(rev(i) > i && arr[rev(i)] > arr[i] + 1) arr[rev(i)] = arr[i] + 1;
		if(arr[i + 1] > arr[i] + 1) arr[i + 1] =  arr[i] + 1;
		// arr[i] = f(i);
		// cerr << i << " " << rev(i) << endl;
		// arr[i] = min(i, arr[rev(i)] + 1);
	}
	// for (int i = MAXN -1; i >= 0; --i)
	// 	// arr[i] = f(i);
	// 	arr[i] = min(i, arr[rev(i)] + 1); 
	cerr <<  "Calculated" << endl;
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		long long n;
		cin >> n;
		cout << "Case #" << test+1 << ": " << arr[n] << endl;
	}
	return 0;
}