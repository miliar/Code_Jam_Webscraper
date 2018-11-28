#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cstdlib>

using namespace std;

int fini[105][105],rowm[105],arr[105][105];

int main(){	
	freopen("F:\\inputsr.in","r",stdin);
	freopen("F:\\outputsr.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		int n,m,cnt;
		cin>>n>>m;
		for(int i=0;i<n;i++){
			rowm[i]=0;
			for(int j=0;j<m;j++){
				cin>>arr[i][j];
				rowm[i]=max(rowm[i],arr[i][j]);
				fini[i][j]=0;
			}
		}
		
		cnt=0;
		
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(arr[i][j]==rowm[i]) {
					fini[i][j] = 1;
					cnt++;
				}
			}
		}
		
		for(int j=0;j<m;j++){
			int flag=1,s=0;
			for(int i=0;i<n && flag;i++){
				if(arr[i][j]!=arr[0][j])
					flag=0; 
				else if(fini[i][j]==0)
					s++;
			}
			if(flag==1) cnt+=s;
		}
		
		if(cnt==n*m)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
