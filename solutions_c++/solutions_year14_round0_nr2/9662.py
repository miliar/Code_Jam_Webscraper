#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<iostream>


using namespace std;

#define rep(i,n) for(int i=0; i<(int)n; i++)
#define st first
#define nd second
#define mp make_pair
#define pb push_back

typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<pi> vpii;
typedef set<int> SI;

#ifdef DEBUG
const bool debug = true;
#else
const bool debug = false;
#endif
int n,m,k,l;
const int inf = 1000 * 1000 * 1000 ;
const int MAKSN = 1000 * 1000 + 13; // UZUPElnic

vector<int> v;

double sum = 0, ans;
double c, f, x, currAns;
double currPr;

double timeSoFar, timeToNext, timeToFinish;
int farmNum = 0;

void zeruj()
{
	sum = 0;
	currPr = 2;
	farmNum = 0;
	ans = 0;
	timeSoFar = 0;
}

void readIn()
{
	zeruj();
	cin>>c>>f>>x;
}


void solve()
{

	ans = x / currPr;

	rep(i, 10000)
	{
		timeToFinish = x / currPr;
		timeToNext = c / currPr;
		ans = min(ans,timeSoFar + timeToFinish);
		timeSoFar += timeToNext;
		currPr += f;
	}

cout.precision(7);
	cout<<fixed<<ans<<"\n";
}

int main()
{
	int test;
	cin>>test;
	rep(i,test)
	{
		cout<<"Case #"<<i+1<<": ";
		readIn();
		solve();
	}
	return 0;
}
