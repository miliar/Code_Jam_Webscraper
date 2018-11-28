// Bismillahirrahmanirrahim
#include <bits/stdc++.h>
using namespace std;
typedef long long int Lint;
typedef pair < Lint , Lint > pii;
typedef pair < Lint , pii > piii;
#define foreach(_i,x)  for(__typeof(x.begin()) _i=x.begin() ; _i != x.end() ; _i++)
#define yeral() (struct node *)calloc(1,sizeof(struct node))
#define all(x) x.begin(),x.end()
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define maxn 100005
#define sc second
#define ft first

Lint N,used[20];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("cikar2.out","w",stdout);
	
	Lint a;
	scanf("%lld",&N);
	
	for ( Lint i = 1 ; i <= N ; i++ ){
		scanf("%lld",&a);
		if ( a == 0 ){
			printf("Case #%lld: INSOMNIA\n",i);
			continue;
		}
		memset(used,0,sizeof used);
		Lint b = 0,top = 0;
		while ( 1 ){
			b += a;
			Lint c = b;
			while ( c ){
				if ( !used[ c%10 ] ){
					top++;
					used[c%10] = 1;
				}
				c /= 10; 
			}
			if ( top == 10 ){
				printf("Case #%lld: %lld\n",i,b);
				break;
			}
		}
	}
	
	return 0;
}
