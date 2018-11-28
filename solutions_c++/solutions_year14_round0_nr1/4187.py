#include <iostream>
using namespace std;

int main() {
	int T,casenum=1;
	cin>>T;
	while (T--) {
		int ans = -1;
		int n1, n2, arr1[4][4], arr2[4][4];
		cin>>n1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin>>arr1[i][j];
		cin>>n2;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin>>arr2[i][j];
		n1--; n2--;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++) {
				//cout<<arr1[n1][i]<<" "<<arr2[n2][j]<<endl;
				if (arr1[n1][i] == arr2[n2][j]) {
					if (ans == -1) ans = arr1[n1][i];
					else ans = -10;
					//cout<<arr1[n1][i]<<" "<<arr2[n2][j]<<" "<<ans<<endl;
				}
			}
		cout<<"Case #"<<casenum++<<": ";
		if (ans == -1) cout<<"Volunteer cheated!"<<endl;
		else if (ans == -10) cout<<"Bad magician!"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}