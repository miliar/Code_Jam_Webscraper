#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main()
{
	//freopen("input.txt","r",stdin);
	freopen(".\\DATA\\codejam_round1B\\B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int z=1; z<=t; z++) {
		int a,b,k,ret=0;
		scanf("%d%d%d",&a,&b,&k);
		for (int i=0; i<a; i++) {
			for (int j=0; j<b; j++) {
				//printf("%d %d %d %d\n",i,j,i&j,(i&j) < k);
				if ((i&j) < k) { ret++; }
			}
		}
		printf("Case #%d: %d\n",z,ret);
	}
}

