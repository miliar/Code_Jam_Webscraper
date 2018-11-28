#include <iostream>
#include <algorithm>
using namespace std;

int X[4];
int Y[4];
int R;
int C[16];
int N;
int A;

int main(){

	int T;

	cin>>T;

	for (int i=1;i<=T;i++){
		N=0;

		cin>>R;
		for (int j=0;j<16;j++) cin>>C[j];
		for (int j=0;j<4;j++) X[j]=C[(R-1)*4+j];
		cin>>R;
		for (int j=0;j<16;j++) cin>>C[j];
		for (int j=0;j<4;j++) Y[j]=C[(R-1)*4+j];

		sort(X,X+4);
		sort(Y,Y+4);

		int j,k;
		j=0;
		k=0;
		while (j<4 && k<4){
			if (X[j] == Y[k]) {
				A=X[j];
				j++;
				k++;
				N++;
				continue;
			}

			if (X[j]<Y[k]) {
				j++;
				continue;
			}

			k++;
		}

		cout<<"Case #"<<i<<": ";

		if (N==0) cout<<"Volunteer cheated!";
		else if (N==1) cout<<A;
		else cout<<"Bad magician!";

		cout<<endl;
	}

	return 0;
}
