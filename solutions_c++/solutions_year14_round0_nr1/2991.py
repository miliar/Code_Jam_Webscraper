#include <iostream>

using namespace std;

int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int ans[2];
		int a[4][4];
		int b[4][4];
		cin>>ans[0];
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin>>a[j][k];
			}
		}
		cin>>ans[1];
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin>>b[j][k];
			}
		}
		int cnt=0;
		int aa;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(a[ans[0]-1][j]==b[ans[1]-1][k]){
					cnt++;
					aa=a[ans[0]-1][j];
				}
			}
		}
		if(cnt==0){
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}else if(cnt==1){
			cout<<"Case #"<<i+1<<": "<<aa<<endl;
		}else{
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}

	}
}