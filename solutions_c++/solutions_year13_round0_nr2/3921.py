#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int i,j,k,l,m,n,t;
int a[100][100];

int main(){
	freopen("output.txt","w",stdout);
	cin>>t;
	for (int T=1;T<=t;T++){
		cin>>m>>n;
		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
				cin>>a[i][j];
		int dd = 1;
		for (i=0;i<m;i++)
			for (j=0;j<n;j++){
				int d = 1;				
				for (k=0;k<n;k++){
					if (a[i][k]>a[i][j]){
						d=0;
						break;
					}
				}
				if (d) continue;
				d = 1;				
				for (k=0;k<m;k++){
					if (a[k][j]>a[i][j]){
						d=0;
						break;
					}
				}
				if (!d) dd = 0;
			}
		if (dd)
			cout<<"Case #"<<T<<": "<<"YES\n"; else
			cout<<"Case #"<<T<<": "<<"NO\n";
	}
	return 0;
}
