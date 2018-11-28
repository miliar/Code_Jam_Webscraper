#include <bits/stdc++.h>
using namespace std;
const int MAX = 1123456;
#define pb push_back
#define sz(a) int((a).size())
#define clr(a,x) memset(a,x,sizeof(a))
typedef pair<int,int> ii;
typedef pair<int, pair<int,int> > iii;
typedef vector<int> vi;
typedef vector< ii > vii;
typedef vector< iii > viii;
typedef vector< vector<int> > vvi;
typedef map< string, int > msi;
#define MAXS 35

char str[MAXS];
int N,J;

int main()
{
	int T, count = 0;
	scanf("%d", &T);
	while ( T-- ) {
		scanf("%d %d", &N, &J);
		for ( int i = 0; i < N; i++ )
			str[i] = '0';
		str[0] = '1'; str[1] = '1'; str[3] = '1'; str[5] = '1'; str[7] = '1'; str[N-1] = '1'; str[N] = 0;
		printf("Case #1:\n");
		for ( int i = 1; i <= 15 && count < 500; i++ ) {
			str[2*i] = '1';
			for ( int j = i+1; j <= 15 && count < 500; j++ ) {
				str[2*j] = '1';
				for ( int k = j+1; k <= 15 && count < 500; k++ ) {
					str[2*k] = '1';
					for ( int m = k+1; m <= 15 && count < 500; m++ ) {
						str[2*m] = '1';
						printf("%s 3 2 5 2 7 2 3 2 11\n", str);
						count++;
						str[2*m] = '0';
					}
					str[2*k] = '0';
				}
				str[2*j] = '0';
			}
			str[2*i] = '0';
		}
	}	
	return 0;
}