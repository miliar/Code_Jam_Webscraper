// saurav shekhar
#include <bits/stdc++.h>

#define MOD 1000000007
#define INF 2000000000
#define EPS 1e-7
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;

const int LIM=10005;


int main(int argc, char* argv[])
{
	int T, qq;
	int s[LIM], X, N;
	scanf("%d",&T);
	for(qq=1; qq<=T; qq++) {
		printf("Case #%d: ", qq);
		scanf("%d %d", &N, &X);
		for(int i=0; i<N; i++) scanf("%d", &s[i]);
		int ans =0, minidx, mins ;
		for(int i=0; i<N; i++) {
			if(s[i] != -1) {
				minidx = i;
				mins = X - s[i];
				for(int j=i+1; j<N; j++) {
					if(s[j] != -1 && X >= s[i] + s[j]) {
						if(X - (s[i] + s[j]) < mins) {
							mins = X - (s[i] + s[j]);
							minidx = j;
						}
					}
				}
				s[minidx] = -1;
				ans++;
			}
		}
		cout << ans << "\n";
		
	}
	
	
	return 0;
}
