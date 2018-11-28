#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef unsigned int ui;
typedef pair<int,int> pii;


#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(int i = (a) - 1; i >= (b); --i)
#define clear(a, b) memset(a, b, sizeof(a))
#define size(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define pb push_back
#define mp make_pair

double C,F,X;





void solve(double prod, double time){

	double tC = C/prod;
	double tX = X/prod;
	double tXC = X/(prod+F);
	double tCX = tC + tXC;

	if(tX<=tCX)	{
		time  =  time + tX;
		cout << fixed << setprecision(7) << time<<endl;
	}
	else{
		solve(prod+F,time+tC);
	}
}

int main()
{
	int t = 0;
	cin >> t;
	FOR(i,0,t)	{
		cout<<"Case #"<<(i+1)<<": ";
		cin >> C;
		cin >> F;
		cin >> X;
		solve(2,0);
	}

	return 0;
};
