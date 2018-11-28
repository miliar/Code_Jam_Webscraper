#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
//#include <string.h>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <functional>


//#include <sstream>
//#include "Biginteger.cpp"
//#include "sqrt.cpp"
//#include "tree.cpp"
//#include "funcs.cpp"

#define ll long long
#define all(x)          (x).begin(), (x).end()
#define forn(N)         for(ll i = 0; i<N; i++)
#define fornj(N)         for(ll j = 0; j<N; j++)
#define PI 3.1415926535897932384626433
#define INF 2147483647
//#define MOD 1000007
using namespace std;


//#define ONLINE_JUDGE
//#undef ONLINE_JUDGE

int arr[10000000];
char tmp[20];
int counter = 0;

bool isPalin(long long x)
{
	counter = 0;
	while(x!=0)
	{
		tmp[counter++] = x%10;
		x/=10;
	}

	for(int i = 0; i<counter; i++)
		if (tmp[i] != tmp[counter-1-i]) return false;

	return true;
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	#endif

	int T;
	cin>>T;
	
	arr[0] = 0;
	for(int it = 1; it<=10000000; it++)
	{
		arr[it] = arr[it-1] + (isPalin(it) && isPalin(it*it));
	}

	long long A, B;

	for(int t = 1; t<=T; t++)
	{
		cin>>A>>B;
		
		long long sqrtA = ceil(sqrt(0.0+A)), sqrtB = floor(sqrt(0.0+B));
		
		cout<<"Case #"<<t<<": "<<arr[sqrtB]-arr[sqrtA-1]<<endl;
	}
	
	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}