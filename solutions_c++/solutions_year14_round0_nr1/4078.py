/*
*
* solved by Ahmed Kamal
*/
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<cstring>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<bitset>
#include<queue>
#include<utility>
#include<algorithm>
#include<functional>

using namespace std;

typedef long long int LL ;
#define vi vector<int> 
#define ii pair<int,int> 
#define vii vector< pair<int,int> > 
#define sc(x) scanf("%d",&x)
double const EPS = 2.22045e-016;
#define INF (1<<29)

#define ALL(v)				((v).begin()), ((v).end())
#define SZ(v)				((int)((v).size()))
#define CLR(v, d)			memset(v, d, sizeof(v))
#define LOOP(i, n)		for(int i=0;i<(int)(n);++i)

#define PB	push_back
typedef vector<double>    VD;
typedef vector<string>    VS;
int gcd(int a, int b) { return (b == 0 ? a : gcd(b, a % b)); }

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
int ha[17];
int t,c,n;
sc(t);
int arr[4][4];
LOOP(ts,t){
	CLR(ha,0);
	sc(c);
	LOOP(i,4)
		LOOP(j,4)
		sc(arr[i][j]);
	LOOP(i,4)
		ha[arr[c-1][i]]++;

		sc(c);
	LOOP(i,4)
		LOOP(j,4)
		sc(arr[i][j]);
	LOOP(i,4)
		ha[arr[c-1][i]]++;

	int p=0,ans=-1;
	LOOP(i,17){
	 if(ha[i]==2){
	  p++;
	  ans = i;
	 }
	}

	bool rep = false;
	switch (p)
	{
	case 0: printf("Case #%d: Volunteer cheated!\n",ts+1);
		rep =true;
		break;
	case 1: printf("Case #%d: %d\n",ts+1,ans);
		rep =true;
		break;
	default:
		break;
	}
	if(!rep)
		printf("Case #%d: Bad magician!\n",ts+1);
}

return 0; 
}
