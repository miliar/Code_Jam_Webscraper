#include <cstdio>
#include <vector>

#define FOR(a,b) for(int a=0; a<b; a++)
#define MAX(a,b) ((a) < (b) ? (b) : (a))

using namespace std;

int T, m, n;

vector < vector < int > > a;
vector < int > mn, mm;

int main (){
	scanf("%d", &T);
	
	FOR(cas, T){
		scanf("%d", &n);
		scanf("%d", &m);
		
		a.resize(n);
		FOR(i, n){
			a[i].resize(m);
			FOR(j, m)
				scanf("%d", &a[i][j]);
		}
		
		mn.resize(n);
		FOR(i, n)
			mn[i]=0;
		mm.resize(m);
		FOR(i, m)
			mm[i]=0;
		
		FOR(i, n)
			FOR(j, m){
				mn[i]=MAX(mn[i], a[i][j]);
				mm[j]=MAX(mm[j], a[i][j]);
			}
		
		int fail=0;
		
		FOR(i, n)
			FOR(j, m)
				if(a[i][j] < mn[i] && a[i][j] < mm[j])
					fail++;
		
/*		FOR(i, n){
			FOR(j, m)
				printf("%d ", a[i][j]);
			printf("\n");
		}
*/		
		
		printf("Case #%d: ", cas+1);
		if(fail)
			printf("NO\n");
		else
			printf("YES\n");
		
	}
	return 0;
}
