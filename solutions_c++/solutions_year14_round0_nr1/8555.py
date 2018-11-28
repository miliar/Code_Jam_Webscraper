#include <bits/stdc++.h>
using namespace std;
#define SZ(V) (long long )V.size()
#define ALL(V) V.begin(), V.end()
#define RALL(V) V.rbegin(), V.rend()
#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i, a, b) for(i = a; i <= b; i++)
#define PB push_back  
#define MP make_pair
#define MOD 1000000007LL
#define no_of_tags 3

typedef pair<int,int> PII;
typedef pair<double, double> PDD;
typedef long long LL;

int main()
{
	LL t,i,j,val,ans1,ans2,test;
	LL grid[4][4];
	cin >> t;
	FORAB(test,1,t)
	{
		LL arr[20]={0},ctr=0;
		cin >> ans1;
		FORN(i,4) FORN(j,4) cin >> grid[i][j];
		FORN(i,4) arr[grid[ans1-1][i]]=1;
		cin >> ans2;
		FORN(i,4) FORN(j,4) cin >> grid[i][j];
		FORN(i,4) if(arr[grid[ans2-1][i]]==1) {ctr++; val = i;}
		cout << "Case #" << test << ": ";
		if(ctr==1) cout << grid[ans2-1][val] << endl;
		else if(ctr>1) cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
	}
	return 0;
}