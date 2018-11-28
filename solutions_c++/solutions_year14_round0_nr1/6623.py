#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cassert>
#include<cstring>
#include<vector>
#include<string>
#include<cmath>
#include<ctime>
#include<set>
#include<map>
 
using namespace std;
 
#define sz(c) (int)(c).size()
 
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
 
#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
 
#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif
 
#define FNAME "1"

int T, a1, a2, a[10][10], b[10][10], Ans, l;
vector <int> ans1, ans2;

int main()
{
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout); 
	scanf("%d", &T);
	for (int g = 0; g < T; g++)
	{
		scanf("%d", &a1);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &a[i][j]);
		scanf("%d", &a2);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &b[i][j]);	
		ans1.clear();
		ans2.clear();
		for (int i = 0; i < 4; i++)
			ans1.pb(a[a1 - 1][i]);    	
		for (int i = 0; i < 4; i++)
			ans2.pb(b[a2 - 1][i]);
		Ans = 0;
   		for (int i = 0; i < 4; i++)
   			for (int j = 0; j < 4; j++)
   				if (ans1[i] == ans2[j])
   				{
   					Ans++;
   					l = ans1[i];
   				}
   		printf("Case #%d: ", g + 1);
   		if (Ans == 0)
   			puts("Volunteer cheated!");
   		if (Ans > 1)
   			puts("Bad magician!");
   		if (Ans == 1)
   			printf("%d\n", l);	
   	} 
    return 0;
}