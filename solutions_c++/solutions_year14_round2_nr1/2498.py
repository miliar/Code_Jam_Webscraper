#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <utility>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

char str[2][101];
struct cnode {
	char c;
	int count;
};

struct cnode a[100];
struct cnode b[100];

int main(int argc, const char *argv[])
{
	int caseNr;
	int caseId;
	scanf("%d", &caseNr);
	for (caseId=0; caseId<caseNr; caseId++) {
		int n;
		int i;
		scanf("%d", &n);
		for (i=0; i<n; i++)
			scanf("%s", str[i]);
		int len1,len2;
		len1=strlen(str[0]);
		len2=strlen(str[1]);

		int var1=0,var2=0;
		for (i=0; i<len1; i++) {
			if (i==0) {
				a[0].c=str[0][0];
				a[0].count=1;
			} else {
				if (str[0][i]==a[var1].c) {
					a[var1].count++;
				} else {
					var1++;
					a[var1].c=str[0][i];
					a[var1].count=1;
				}
			}
		}
		for (i=0; i<len2; i++) {
			if (i==0) {
				b[0].c=str[1][0];
				b[0].count=1;
			} else {
				if (str[1][i]==b[var2].c) {
					b[var2].count++;
				} else {
					var2++;
					b[var2].c=str[1][i];
					b[var2].count=1;
				}
			}
		}
		/*
		int count=0;
		int flag=0;
		while (j<len1 && k<len2) {
			if (str[1][k] == str[0][j]) {
				k++;
				j++;
			} else {
				if (j>0 && str[0][j]==str[0][j-1]) {
					count++;
					j++;
				}
				if (k>0 && str[1][k]==str[1][k-1]) {
					count++;
					k++;
				}
				flag=1;
				break;
			}
		}
		*/
		//for (i=0; i<var1; i++) {
		//	printf("a[%d].c=%c, a[%d].count=%d\n", i, a[i].c, i, a[i].count);
		//}
		//for (i=0; i<var2; i++) {
		//	printf("b[%d].c=%c, b[%d].count=%d\n", i, b[i].c, i, b[i].count);
		//}

		if (var1 != var2) {
			printf("Case #%d: %s\n", caseId+1, "Fegla Won");
			continue;
		}
		int dcount=0;
		for (i=0; i<=var1; i++) {
			if (a[i].c != b[i].c) {
				dcount=-1;
				break;
			} else {
				dcount+=abs(a[i].count-b[i].count);
			}
		}
		if (dcount==-1)
			printf("Case #%d: %s\n", caseId+1, "Fegla Won");
		else
			printf("Case #%d: %d\n", caseId+1, dcount);
	}
	return 0;
}
