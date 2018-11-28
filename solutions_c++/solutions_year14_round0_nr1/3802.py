#include <cstdio>

#define MAXN 105
#define forn(i,n) for(int i = 0; i < n; i++)
#define forn2(i,j,n) for(int i = j; i <= n; i++)

using namespace std;

int row1[4], row2[4];

void readRows(int n){
	int i,j,a;
	forn(i,n) forn(j,4) scanf("%d",&a);
}

int main(){
	int T,t;
	scanf("%d",&T);
	forn2(t,1,T){
		int r1, r2;
		scanf("%d",&r1);
		int j,k;
		readRows(r1-1);
		forn(j,4) scanf("%d",&row1[j]);
		readRows(4-r1);

		scanf("%d",&r2);

		readRows(r2-1);
		forn(j,4) scanf("%d",&row2[j]);
		readRows(4-r2);

		int count = 0, res;
		forn(j,4)
			forn(k,4)
				if(row1[j] == row2[k]){
					count++;
					res = row2[k];
				}

		printf("Case #%d: ",t);
		if(count == 0)
			printf("Volunteer cheated!\n");
		else if(count == 1)
			printf("%d\n",res);
		else printf("Bad magician!\n");
	}
}