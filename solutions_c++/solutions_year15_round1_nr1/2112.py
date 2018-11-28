#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long
int A[10000];
#undef int
int main()
{
#define int long long
	int t,n; scanf("%llu",&t);
	int a,b,diff,mdiff;
	for (int tt = 1; tt <= t; tt++)
	{
		a=0;
		b=0;
		cerr << "Executing Case #" << tt << "\n";
		scanf("%llu",&n);
		diff=0;mdiff=0;
		for(int i=0;i<n;i++){
			scanf("%llu",&A[i]);
			if(A[i]<A[i-1]){
				diff=(A[i-1]-A[i]);
				a+=diff;
				if(diff>mdiff)
					mdiff=diff;
			}
		}
		for(int j=0;j<(n-1);j++){
		b+=(A[j]>mdiff)?mdiff:A[j];
		}
		cout << "Case #" << tt << ": " <<a<<" "<<b<< "\n";
	}
	return 0;
}
