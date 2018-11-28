#include <iostream>
#include <cstring>
#include <string>
using namespace std;
int a[18];
int b[5][5];
int main(){
	int T, cas = 0;
	for (cin>>T; T--; ){
		memset(a, 0, sizeof(a));
		int p;
		cin>>p;
		for (int i = 1; i<=4; i++){
			for (int j = 1; j<=4; j++){
				cin>>b[i][j];
			}
		}
		for (int i = 1; i<=4; i++){
			a[b[p][i]]++;
		}
		cin>>p;
		for (int i = 1; i<=4; i++){
			for (int j = 1; j<=4; j++){
				cin>>b[i][j];
			}
		}
		for (int i = 1; i<=4; i++){
			a[b[p][i]]++;
		}
		int fd =-1;
		int cnt = 0;
		for (int i = 1; i<=16; i++){
			if (a[i] == 2){
				fd = i;
				cnt++;
			}
		}
		++cas;
		cout<<"Case #"<<cas<<": ";
		if (cnt == 0){
			cout<<"Volunteer cheated!"<<endl;
		}
		if (cnt > 1){
			cout<<"Bad magician!"<<endl;
		}
		if (cnt == 1){
			cout<<fd<<endl;
		}
	}
	return 0;
}



