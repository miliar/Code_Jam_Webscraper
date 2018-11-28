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

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("cikar.out","w",stdout);
	
	int a,b,c;
	cin >> T;
	
	for ( int i = 1 ; i <= T ; i++ ){
		scanf("%d %d %d",&a,&b,&c);
		
		printf("Case #%d: ",i);
		for ( int j = 1 ; j <= c;  j++ )
			printf("%d ",j);
		puts("");			
	}
	
	return 0;
}
