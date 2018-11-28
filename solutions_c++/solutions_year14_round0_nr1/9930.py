#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int testCases=1;testCases<=t;testCases++){
		int f,l;
		int arr[4][4];
		scanf("%d",&f);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&arr[i][j]);
			}
		}
		int row1[4];
		for(int i=0;i<4;i++){
			row1[i]=arr[f-1][i];
		}
		scanf("%d",&l);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&arr[i][j]);
			}
		}
		int row2[4];
		for(int i=0;i<4;i++){
			row2[i]=arr[l-1][i];
		}
		int ans=-1;
		int n=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(row1[i]==row2[j]){
					ans=row1[i];
					n++;
				}
			}
		}
		cout<<"Case #"<<testCases<<": ";
		if(n==0){
			cout<<"Volunteer cheated!"<<endl;
		}
		else if(n==1){
			cout<<ans<<endl;
		}
		else{
			cout<<"Bad magician!"<<endl;
		}
	}
	return 0;
}
