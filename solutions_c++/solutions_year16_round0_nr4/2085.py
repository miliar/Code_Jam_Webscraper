#include <bits/stdc++.h>
using namespace std;
const int MAX = 1123456;
#define pb push_back
#define sz(a) int((a).size())
#define clr(a,x) memset(a,x,sizeof(a))
typedef pair<int,int> ii;
typedef pair<int, pair<int,int> > iii;
typedef vector<int> vi;
typedef vector< ii > vii;
typedef vector< iii > viii;
typedef vector< vector<int> > vvi;
typedef map< string, int > msi;

int main()
{
	int T, K, C, S;
	int tc = 1;
	scanf("%d", &T);
	while ( T-- ) {
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d:", tc++);
		for ( int i = 1; i <= S; i++ )
			printf(" %d", i);
		printf("\n");
	}
	return 0;
}
