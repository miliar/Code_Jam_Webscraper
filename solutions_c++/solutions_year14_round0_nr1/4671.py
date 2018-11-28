#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_SIZE 2000

int a[4][4];
int b[4][4];

int main(int argc, const char *argv[])
{
	int caseNr;
	int caseId;
	scanf("%d", &caseNr);
	for (caseId=0; caseId<caseNr; caseId++) {
		int m,n,i,j;

		scanf("%d", &m);
		for (i=0; i<4; i++) 
			for (j=0; j<4; j++) 
				scanf("%d", &a[i][j]);
		scanf("%d", &n);
		for (i=0; i<4; i++) 
			for (j=0; j<4; j++) 
				scanf("%d", &b[i][j]);

		int *p, *q;
		p = find_first_of(&a[m-1][0], &a[m-1][3]+1, &b[n-1][0], &b[n-1][3]+1);
		if (p == &a[m-1][3]+1) {
			printf("Case #%d: %s\n", caseId+1, "Volunteer cheated!");
		} else {
			q = find_first_of(p+1, &a[m-1][3]+1, &b[n-1][0], &b[n-1][3]+1);
			if (q == &a[m-1][3]+1) {
				printf("Case #%d: %d\n", caseId+1, *p);
			} else {
				printf("Case #%d: %s\n", caseId+1, "Bad magician!");
			}
		}
	}
	return 0;
}
