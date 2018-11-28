#include <bits/stdc++.h>


using namespace std;


double x[1111];
double y[1111];
double z[1111];


double dist(int a,int b){
	return sqrt( (x[a]-x[b])*(x[a]-x[b]) + (y[a]-y[b])*(y[a]-y[b]) + (z[a]-z[b])*(z[a]-z[b]) );
}


double ans[1111][1111];

int main(){
	freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    
	int t;
	cin>>t;
	
	int cas = 0;
	while(t--){
		cas++;
		int n,s;
		cin>>n>>s;
		
		for(int i=1;i<=n;i++){
			cin>>x[i]>>y[i]>>z[i];
			int q,w,e;
			cin>>q>>w>>e;
		}
		
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				ans[i][j] = dist(i,j);
			}
		}
		
		for(int k=1;k<=n;k++){
			for(int i=1;i<=n;i++){
				for(int j=1;j<=n;j++){
					ans[i][j] = min(ans[i][j],max(ans[i][k],ans[k][j]));
				}
			}
		}
		
		printf("Case #%d: %.10f\n",cas,ans[1][2]);

		
	}
	
	
	return 0;
}
