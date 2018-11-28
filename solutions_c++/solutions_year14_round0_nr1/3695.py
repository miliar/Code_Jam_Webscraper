#include <iostream>
using namespace std;

int main(){
	int n;
	cin>>n;
	for(int t=0;t<n;t++){
		int arr[4][4];
		int brr[4][4];
		int a,b;
		cin>>a;
		a--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>arr[i][j];
			}
		}
		cin>>b;
		b--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>brr[i][j];
			}
		}
		int ans;
		bool found = false;
		bool bad = false;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(arr[a][i]==brr[b][j]){
					if(!found){
						found = true;
						ans = arr[a][i];
					}
					else {
						bad = true;
						break;
					}
				}
			}
		}
		if(bad) {
			cout<<"Case #"<<t+1<<": Bad magician!\n";
		}
		else if(!found){
			cout<<"Case #"<<t+1<<": Volunteer cheated!\n";
		}
		else cout<<"Case #"<<t+1<<": "<<ans<<endl;
}
}
