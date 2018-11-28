// dtb @ gcj'13
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

#define INFILE "./B-large.in"
#define OUTFILE "./Blarge2"

using namespace std;

int main () {


		freopen (INFILE,"r",stdin);
		freopen (OUTFILE,"w+",stdout);
		
		int a[100][100],mc[100],mr[100];

		int T,caseNum=0,flag,n,m,max;

		for (scanf("%d",&T);T;T--) {
				// input
				scanf ("%d %d",&n,&m);
				for (int i=0;i<n;i++)
						for (int j=0;j<m;j++)
								scanf ("%d",&a[i][j]);

				// process
				for (int i=0;i<n;i++) {
						max=0;
						for (int j=0;j<m;j++) {
								if (max < a[i][j])
										max=a[i][j];
						}
						mr[i]=max;
				}
				
				for (int i=0;i<m;i++) {
						max=0;
						for (int j=0;j<n;j++) {
								if (max < a[j][i])
										max=a[j][i];
						}
						mc[i]=max;
				}

				flag=0;
				for (int i=0;i<n;i++) {
						for (int j=0;j<m;j++) {
								if (a[i][j] < mc[j] && a[i][j] < mr[i]) {
										flag=1;
										break;
								}
						}
						if (flag)
								break;
				}

				// output
				printf ("Case #%d: ",++caseNum);
				if (flag)
						printf ("NO\n");
				else printf ("YES\n");
		}
}

