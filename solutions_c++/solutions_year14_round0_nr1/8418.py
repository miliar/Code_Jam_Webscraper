#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
const int maxn = 1000000 + 10;
typedef long long LL;
int one[100][100],two[100][100];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int o,testc,ca=0,t;
	int count=0;
    scanf("%d", &testc);
	int found;
    while (testc--) {
		count=0;
        printf("Case #%d: ", ++ca);
        scanf("%d\n",&o);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&one[i][j]);
		scanf("%d",&t);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&two[i][j]);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				if(one[o-1][i]==two[t-1][j]){
					count++;
					found=one[o-1][i];
				}

			}
        if(count==1)
			printf("%I64d\n", found);
		else if(count>1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
    }
    return 0;
}

