#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

#define rep(i,n) for(int i = 0; i < (n); i++)

const int N = 100;
int a[N][N];

void runCase()
{
	int n,m;
	scanf("%d %d", &n, &m);
	rep(i,n) rep(j,m) scanf("%d",&a[i][j]);
	
	rep(i,n) rep(j,m) {
		bool can = true;
		rep(k,n) if(a[k][j] > a[i][j]) can = false;
		if(!can) {
			can = true;
			rep(k,m) if(a[i][k] > a[i][j]) can = false;
			
			if(!can) {
				//printf("%d %d\n",i,j);
				printf("NO\n");
				return;
			}
		}
	}
	printf("YES\n");
}

void runSample()
{
	string input;

	char buf[501] = {0};
	cin.getline(buf,501);

	input = buf;


	printf("%s\n",input.c_str());
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();

	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
		//runSample();
	}
}

int main()
{
	solve();
	return 0;
}
