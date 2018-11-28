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

int main(int argc, const char *argv[])
{
	int caseNr;
	int caseId;
	scanf("%d", &caseNr);
	for (caseId=0; caseId<caseNr; caseId++) {
		int a,b,k;
		scanf("%d %d %d", &a,&b,&k);
		int res=0,i,j;
		for (i=0;i<a;i++)
			for(j=0;j<b;j++) {
				if ((i&j) < k)
					res++;
			}

		printf("Case #%d: %d\n", caseId+1, res);
	}
	return 0;
}
