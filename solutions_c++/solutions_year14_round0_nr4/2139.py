#include<stdio.h>
#include<algorithm> 

using namespace std;

double cards[2][1100];
bool cmp (double i, double j) { return (i>j); }

int main() {

	int T,N;
	int num=1,i,j,k,ans1,ans2;

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	scanf("%d", &T);
	while(T-->0) {
		scanf("%d", &N);
		for(i=0 ; i<2 ; i++) for(j=0 ; j<N ; j++) scanf("%lf", &cards[i][j]);
		sort(cards[0], cards[0]+N, cmp); sort(cards[1], cards[1]+N, cmp);

		for(i=N-1,j=0,k=N-1 ; i>=0 ; i--)
			(cards[0][i]<cards[1][k])?j++:k--;
		ans1 = N-1-k;	

		for(i=0,j=0,k=N-1 ; i<N ; i++)
			(cards[0][i]>cards[1][j])?k--:j++;
		ans2 = N-1-k;		

		printf("Case #%d: ", num++);
		printf("%d %d\n", ans1, ans2);
	}

	return 0;
}