#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;

int n;
int main(void) {
	int t, ca = 1;
	cin >> t;
	while( t-- ) {
		cin >> n;
		vi vec(n+1), s(n+1,0);
		int ans=0,sum = 0;
		for( int i = 0; i<=n; i++ )
		{
			int tmp;
			scanf("%1d", &tmp );
			vec[i] = tmp;
			if( sum < i ) {
				ans += i-sum;
				vec[i] += i-sum;
			}
			sum += vec[i];
		}
		cout << "Case #" << ca++ << ": ";
		cout << ans << "\n";
	}

	return 0;
}
