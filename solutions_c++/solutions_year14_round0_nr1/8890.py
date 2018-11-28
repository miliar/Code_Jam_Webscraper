#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	int k=1;
	while(t--) {
		cout<<"Case #"<<k<<": ";
		k++;
		int row1,row2;
		int arr1[4][4],arr2[4][4];
		cin>>row1;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				cin>>arr1[i][j];
			}
		}
		cin>>row2;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				cin>>arr2[i][j];
			}
		}
		int countMatch = 0;
		int rowele[4];
		for(int i=0;i<4;i++) {
			rowele[i]=arr1[row1-1][i];
		}
		int index;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				if(rowele[i]==arr2[row2-1][j])
					{
						countMatch++;
						index = i;
						break;
					}
			}
		}
		if(countMatch==1) {
			cout<<rowele[index]<<endl;
		}
		else if(countMatch==0) {
			cout<<"Volunteer cheated!"<<endl;
		}
		else if(countMatch>1) {
			cout<<"Bad magician!"<<endl;
		}
		
	}
	return 0;
}