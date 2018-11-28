#include<iostream>
#include<cstdio>
using namespace std;
int table1[4][4], table2[4][4];
int main(){
	int T;
	int times=0;
	cin>>T;
	while(times++<T){
		int a,b;
		int ans=0,flg=0;
		cin>>a;a--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>> table1[i][j];
			}
		}
		cin>>b;b--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>> table2[i][j];
			}
		}
		
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(table1[a][j]==table2[b][k]){
					ans=table1[a][j];flg++;
				}
			}
		}
		if(flg==1){
			printf("Case #%d: %d\n",times,ans);
		}else if(flg>1){
			printf("Case #%d: %s\n",times,"Bad magician!");
		}else{
			printf("Case #%d: %s\n",times,"Volunteer cheated!");
		}
	}
	return 0;
}
