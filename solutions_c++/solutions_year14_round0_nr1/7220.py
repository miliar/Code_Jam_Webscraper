#include <cstdio>
#include <cstring>

int t;
int a[4][4], b[4][4];
int aa, bb;
int arr[16];

int main()
{
	scanf("%d",&t);
	for (int cas=1; cas<=t; ++cas) {
		scanf("%d",&aa);
		for (int i=0; i<4; ++i) for (int j=0; j<4; ++j) scanf("%d",&a[i][j]);
		scanf("%d",&bb);
		for (int i=0; i<4; ++i) for (int j=0; j<4; ++j) scanf("%d",&b[i][j]);
		memset(arr,0,sizeof(arr));
		for (int i=0; i<4; ++i) ++arr[a[aa-1][i]-1];
		for (int i=0; i<4; ++i) ++arr[b[bb-1][i]-1];
		int num = 0;
		int n = 1;
		for (int i=0; i<16; ++i) {
			if (arr[i]==2) {
				++num;
				n = i;
			}
		}
		printf("Case #%d: ",cas);
		if (num==1) printf("%d\n",n+1);
		else if (num==0) puts("Volunteer cheated!");
		else puts("Bad magician!");
	}
	return 0;
}
