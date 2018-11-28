#include<iostream>
using namespace std;

int f[109][109];
int ma[109][109];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("AC.out","w", stdout);
	int cas;
	int ca=1,n,m;
	scanf("%d", &cas);
	
	while(cas--){
		scanf("%d%d", &n, &m);
		
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				scanf("%d", &f[i][j]);
				ma[i][j] = 100;
			}
		}
		for(int i=0; i<n; i++){
			int mmax = f[i][0];
			for(int j=1; j<m; j++)
				mmax = max(mmax, f[i][j]);
			for(int j=0; j<m; j++){
				if(ma[i][j] > mmax)
					ma[i][j] = mmax;
			}
		}
		for(int j=0; j<m; j++){
			int mmax = f[0][j];
			for(int i=1; i<n; i++){
				mmax = max(mmax, f[i][j]);
			}
			for(int i=0; i<n; i++){
				if(ma[i][j] > mmax)
					ma[i][j] = mmax;
			} 
		}
		int sign = 1;
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++){
				if(ma[i][j] != f[i][j])
					sign = 0;
			}
		if(sign)
			printf("Case #%d: YES\n",ca++);
		else
			printf("Case #%d: NO\n",ca++);
	}
	return 0;
}
