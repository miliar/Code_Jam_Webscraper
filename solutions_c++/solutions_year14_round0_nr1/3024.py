#include <cstdio>
#include <algorithm>
using namespace std;
int tc,a[4][4],b[4][4],c,d;
int cnt[20],tcn;
int main(void){
	//freopen("A-small-attempt0.in","r",stdin);
//	freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	while(tc--){
		scanf("%d",&c);
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++)
				scanf("%d",&a[i][j]);
		}
		scanf("%d",&d);
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++)
				scanf("%d",&b[i][j]);
		}
		fill(cnt,cnt+20,0);
		for(int j=0; j<4; j++){
			cnt[a[c-1][j]]++;
			cnt[b[d-1][j]]++;

		}
		int re=0;
		for(int i=1; i<=16; i++){
			if(!re && cnt[i]==2)
				re=i;
			else if(re && cnt[i]==2)
				re=20;
		}
		printf("Case #%d: ",++tcn);
		if( re == 20 )
			puts("Bad magician!");
		else if( ! re )
			puts("Volunteer cheated!");
		else
			printf("%d\n",re);
	}

	return 0;
}