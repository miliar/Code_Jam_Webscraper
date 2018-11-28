#include <iostream>

using namespace std;

int main(){
	int num, n;
	cin >> num;
	for (int i=0; i<num; i++){
		int r[4];
		int row1, r1[4];
		cin >> row1;
		for(int j=0; j<row1; j++){
			for(int k=0; k<4; k++)
				cin>>r1[k];
		}
		for(int j=row1; j<4; j++){
			for(int k=0; k<4; k++)
				cin>>n;
		}
		int row2, r2[4];
		cin >> row2;
		for(int j=0; j<row2; j++){
			for(int k=0; k<4; k++)
				cin>>r2[k];
		}
		for(int j=row2; j<4; j++){
			for(int k=0; k<4; k++)
				cin>>n;
		}
		int count=0;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				if(r1[j]==r2[k]){
					r[count]=r1[j];
					count++;
				}				
			}
		}
		if(count==0) cout << "Case #"<< i+1 <<": Volunteer cheated!" << endl;
		else if(count>1) cout << "Case #"<< i+1 <<": Bad magician!" << endl;
		else cout << "Case #"<< i+1 <<": " << r[0] << endl;
	}
}
