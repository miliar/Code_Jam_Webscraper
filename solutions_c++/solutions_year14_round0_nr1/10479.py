#include <iostream>
using namespace std;
int a[5][5],b[5][5];
int main(){
	int t,x,y,z;
	cin >> t;
	for(int idx=1;idx<=t;idx++){
		cin >> x;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin >> a[i][j];
			}
		}
		cin >> y;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin >> b[i][j];
			}
		}
		int cnt=0;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				if(a[x][i]==b[y][j])cnt++,z=j;
			}
		}
		cout<<"Case #"<<idx<<": ";
		if(cnt==1) cout<<b[y][z]<<endl;
		else if(cnt==0) cout<<"Volunteer cheated!\n";
		else cout<<"Bad magician!\n";
	}
}