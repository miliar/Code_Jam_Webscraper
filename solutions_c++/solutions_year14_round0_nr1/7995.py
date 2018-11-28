//Problem A. Magic Trick
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <cmath>
using namespace std;
#define ll int
#define INF 1000000000
#define debug puts("DEBUUGG")
#define vi vector<ll>
#define pii pair<ll,ll>
#define vii vector<pii>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define rep(a,b,c) for(a=b;a<c;a++)
#define repe(a,b,c) for(a=b;a<=c;a++)
#define repd(a,b,c) for(a=b-1;a>=c;a--)
#define ALL(a) a.begin(),a.end()

int total,row,ar[20];
int solve(int tc){
	int temp,ans;
	scanf("%d",&row);
	for (int i = 1; i < 5; ++i){
		for (int j=1; j < 5; ++j){
			scanf("%d",&temp);
			if(i==row)
				ar[temp]++;
		}
	}
	scanf("%d",&row);
	for (int i = 1; i < 5; ++i){
		for (int j=1; j < 5; ++j){
			scanf("%d",&temp);
			if(i==row)
				if (ar[temp]==1) {
					++total;
					ans = temp;
				}

		}
	}

	printf("Case #%d: ",tc);
	if (total==0) puts("Volunteer cheated!");
	else if (total==1) printf("%d\n",ans);
	else puts("Bad magician!");

}
int main(int argc, char const *argv[])
{
	/* code */
	int tc;
	scanf("%d",&tc);
	for (int i = 1; i <= tc; ++i)
	{
		// bersihkan array
		for (int j = 0; j < 17; ++j)
		{
			ar[j]=0;
			/* code */
		}
		total = 0;
		/* code */
		solve(i);
	}
	
	return 0;
}
