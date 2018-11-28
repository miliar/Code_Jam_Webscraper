#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
const int MNAX = 100;
int a[MNAX][MNAX];
int p[MNAX][MNAX];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	long long n,i,j;
	int test;
	cin>>test;
	
	for (int t=1;t<=test;++t){
		int n,m;
		cin>>n>>m;
		for (int i=0;i<n;++i){
			for (int j=0;j<m;++j){
				cin>>p[i][j];
				a[i][j] = 100;
			}
		}
		for (int i=0;i<n;++i){
			int max = 0;
			for (int j=0;j<m;++j){
				if (p[i][j] > max) max = p[i][j];
			}
			for (int j=0;j<m;++j){
				if (a[i][j] > max) a[i][j] = max;
			}
		}

		for (int i=0;i<m;++i){
			int max = 0;
			for (int j=0;j<n;++j){
				if (p[j][i] > max) max = p[j][i];
			}
			for (int j=0;j<n;++j){
				if (a[j][i] > max) a[j][i] = max;
			}
		}

		string ans = "YES";
		for (int i=0;i<n;++i){
			for (int j=0;j<m;++j){
				if (a[i][j] != p[i][j]) ans = "NO";
			}
		}

		cout<<"Case #"<<t<<": "<<ans<<'\n';
	}

	return 0;
}