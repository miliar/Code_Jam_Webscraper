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

int t[20];
vector<int> v;
void zeruj()
{
	rep(i,20)
		t[i] = 0;
}

void readIn()
{

	v.clear();

	rep(ii,2)
	{
	scanf("%d",&k);

	k--;
	rep(i,4)
	{
		rep(j,4)
		{
			scanf("%d",&l);

			if(i==k)
			{
				t[l] ++;
			}

		}
	}
	}
}


void solve()
{


	rep(i,20)
		if(t[i] == 2)
			v.pb(i);

	if(v.size() == 1)
		printf("%d \n",v[0]);
	if(v.size() == 0)
		printf("Volunteer cheated!\n");
	if(v.size() > 1)
		printf("Bad magician!\n");

	zeruj();

}

int main()
{
	int test;
	scanf("%d",&test);
	rep(i,test)
	{
		printf("Case #%d: ",i+1);
		readIn();

		solve();
	}
	return 0;
}
