#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

const int MM = 2500 + 10;
const int NN = 55;
int tmp[MM];
int N;
int main (){
	freopen ("F:\\GCJ\\R1\\B-large.in", "r",stdin);
	freopen ("F:\\GCJ\\R1\\B-large.out", "w",stdout);
	
	int cas = 1, a;
	int T;scanf ("%d",&T);
	while (T--){
		printf ("Case #%d:",cas++);
		scanf ("%d", &N);
		int MA = 2 * N - 1;
		memset (tmp, 0, sizeof(tmp));
		for (int i=0;i<MA;i++){
			for (int j=0;j<N;j++)	scanf ("%d",&a), tmp[a] ^= 1;
		}
		for (int i=1;i<MM;i++){
			if (tmp[i])
				printf (" %d",i);
		}
		printf ("\n");
	}
	return 0;
}