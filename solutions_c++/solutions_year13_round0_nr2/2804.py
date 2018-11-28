#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int main(){	
	freopen("F:\\input2.in","r",stdin);
	freopen("F:\\output2.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int I=1;I<=t;I++){
		printf("Case #%d: ",I);
		int n,m;
		cin>>n>>m;
		int done[n][m];
		int rMax[n];
		int arr[n][m];
		for(int i=0;i<n;i++){
			int ma=0;
			for(int j=0;j<m;j++){
				done[i][j]=0;
				cin>>arr[i][j];
				ma=max(ma,arr[i][j]);
			}
			rMax[i]=ma;
		}
		int ok=0;
		for(int i=0;i<n;i++){
			int num = rMax[i];
			for(int j=0;j<m;j++){
				if(arr[i][j]==num) {
					ok++;
					done[i][j] = 1;	
				}
			}
		}
		//cout<<ok<<endl;
		for(int j=0;j<m;j++){
			int pre=arr[0][j];
			int fl=1;
			int add=0;
			for(int i=0;i<n && fl;i++){
				if(arr[i][j]!=pre) fl=0; 
				else if(done[i][j]==0) add++;
			}
			if(fl) ok+=add;
		}
		//cout<<ok;
		
		if(ok==n*m) puts("YES");
		else puts("NO");
		
	}
	return 0;
}
