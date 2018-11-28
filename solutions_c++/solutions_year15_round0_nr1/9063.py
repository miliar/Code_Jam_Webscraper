/************************************************************/
// 	Author  : Krishna Vedulla
//	College : Army Institute of Technology, Pune
/************************************************************/

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <limits.h>
#include <algorithm>
#include <math.h>
#include <map>
#include <list>
#include <bitset>
#include <set>
#include <fstream>
#include <string.h>


#define MAX 1010
#define MOD 1000000007
#define LL long long
#define ULL unsigned long long


#define FOR(i,a,b) for(int i=a; i<b; i++)
#define FOR_(i,a,b) for(int i=a-1; i>=b; i--)
#define NODE pair<int, int>
#define SQR(a) ((a)*(a))
#define VI vector<int>
#define MII map<int, int>

#define SI(n) scanf("%d", &n)
#define SS(r) scanf("%s", r)
#define PI(n) printf("%d\n", n)
#define PS(r) printf("%s\n", r)

using namespace std;

/*********************************************************************************/

int solve(char *a, int n)
{
	int ans = 0, k ;
	// processing
	int tot = a[0] - '0';
	for(int i=1; i<=n; i++){
		
		if(tot < i){
			k = i-tot;
			ans += k;
			tot += k;
		}
		tot += a[i] - '0';
	}

	return ans;
}

int main()
{
	int t, n, ans;
	char a[MAX];
	ifstream fin;
	ofstream fout;
	fin.open("standing ovation - Bigip.txt");
	fout.open("standing ovation - Bigop.txt");

	fin >> t;
	for(int i = 1; i <= t; i++)
	{
		ans = 0;
		fin >> n >> a;
		ans = solve(a,n);
		fout << "Case #" << i << ": " << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}