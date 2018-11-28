#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int tcno=1;tcno<=t;tcno++){
		int m,n;
		scanf("%d %d",&m,&n);
		int board[m][n];
		for(int i=0;i<m;i++){
			for(int j=0;j<n;j++){
				scanf("%d",&board[i][j]);
			}
		}
		int possible=1;
		
		for(int i=0;i<m;i++){
			for(int j=0;j<n;j++){
				bool flag=false;
				for(int k=0;k<m;k++){
					if(board[i][j]<board[k][j]){
						flag=true;
						break;
					}
				}
				if(flag){
					for(int k=0;k<n;k++){
						if(board[i][j]<board[i][k]){
							possible=0;
							break;
						}
					}
				}
				if(possible==0){
					break;
				}
			}
		}
		
		if(possible){
			printf("Case #%d: YES\n",tcno);
		}
		else{
			printf("Case #%d: NO\n",tcno);
		}
	}
}
