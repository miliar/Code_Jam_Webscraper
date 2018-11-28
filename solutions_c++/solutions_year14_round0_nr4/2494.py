#include<stdio.h>
#include<algorithm>
using namespace std;

double A[1005];
double B[1005];
int visit[1005];
int main()
{
	int T;
	int Case = 1;
	scanf("%d", &T);
	while ( T-- ) {
		int N;
		scanf("%d", &N);
		for ( int i = 0 ; i < N ; i++ ) {
			scanf("%lf", &A[i]);
		}
		for ( int i = 0 ; i < N ; i++ ) {
			scanf("%lf", &B[i]);
		}
		for ( int i = 0 ; i < N ; i++ ) {
			visit[i] = 0;
		}
		sort(A,A+N);
		sort(B,B+N);
		int win;
		win = 0;
		for ( int i = N-1 , j = N-1 ; i >= 0 && j >= 0 ; ) {
			while ( j >= 0 && B[j] > A[i] ) {
				j--;
			}
			if ( j < 0 )
				break;
			win++;
			i--;
			j--;
		}
		printf("Case #%d: %d", Case++, win);

		win = 0;		
		int leftmost = 0;
		for ( int i = 0 ; i < N ; i++ ) {
			int flag = 0;
			for ( int j = 0 ; j < N ; j++ ) {
				if ( !visit[j] && B[j] > A[i] ) {
					visit[j] = 1;
					flag = 1;
					break;
				}
			}
			if ( !flag ) {
				win++;
				while ( visit[leftmost] ) {
					leftmost++;
				}
				visit[leftmost] = 1;
			}			
		}
		printf(" %d\n", win);
	}
	return 0;
}
