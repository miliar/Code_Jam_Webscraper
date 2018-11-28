#include <iostream>
#include <string>
#include <iostream>
#include <iostream>
#include <iostream>
#include <iostream>

using namespace std;

#define rep(i,n) for( int i = 0; i < (n); i++ )

const int MXN = 110;

int a [MXN][MXN];
int mx [MXN][2];

string solve(){

	int n,m;
	scanf("%d%d", &n, &m);

	rep(i,n) mx[i][0] = 0;
	rep(j,m) mx[j][1] = 0;

	rep(i,n)
		rep(j,m){
			scanf("%d", &a[i][j]);
			mx[i][0] = max(mx[i][0], a[i][j]);
			mx[j][1] = max(mx[j][1], a[i][j]);
		}

	rep(i,n) rep(j,m) if( a[i][j]!=mx[i][0] && a[i][j]!=mx[j][1] ) return "NO";
	return "YES";
}

int main(){

	freopen("B.txt", "r", stdin);	freopen("B.out", "w", stdout);


	int T;
	scanf("%d", &T);

	for( int i = 0; i < T; i++ ){
		printf("Case #%d: ", i+1);
		cout<<solve()<<endl;
	}

}