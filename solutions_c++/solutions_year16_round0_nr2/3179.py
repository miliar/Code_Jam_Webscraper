// Bismillahirrahmanirrahim
#include <bits/stdc++.h>
using namespace std;
typedef long long int Lint;
typedef pair < int , int > pii;
typedef pair < int , pii > piii;
#define foreach(_i,x)  for(__typeof(x.begin()) _i=x.begin() ; _i != x.end() ; _i++)
#define yeral() (struct node *)calloc(1,sizeof(struct node))
#define all(x) x.begin(),x.end()
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define maxn 100005
#define sc second
#define ft first

int T;
inline void yaz (int i , int x ){
	printf("Case #%d: %d\n",i,x);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	ios_base::sync_with_stdio(0);
	cin >> T;
	
	for ( int i = 1 ; i <= T ; i++ ){
		
		string str;
		cin >> str;
		int uz = str.size();
		
		int ans = 0 , last = 0;
		
		for ( int j = 0 ; j < uz ; j++ )
			if ( j != uz-1 && str[j] != str[j+1] )
				ans++;
		if ( str[uz-1] == '-' )
			ans++;
		
		yaz ( i , ans );
		
	}
	
	return 0;
}
