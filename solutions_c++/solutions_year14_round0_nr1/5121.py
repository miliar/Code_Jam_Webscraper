#include <iostream>
#include <string>
using namespace std;

int main(){
	int r1,r2,n;
	int array1[4][4], array2[4][4];
	cin>>n;
	std::string output[n];
	for(int k=1; k<= n; k++){
		cin>>r1;
		for (int a=0; a<4; a++){
			for (int b=0; b<4; b++){
				cin>>array1[a][b];
			}
		}
		cin>>r2;
		for (int a=0; a<4; a++){
			for (int b=0; b<4; b++){
				cin>>array2[a][b];
			}
		}
		int count = 0;
		int num;
		for (int i=0; i<4; i++){
			for (int j=0; j<4; j++){
				if (array1[r1-1][i] == array2[r2-1][j]){
					count++;
					num = array1[r1-1][i];
				}
			}
		}
		string s;
		if (count == 1){
			s="Case #" + std::to_string(k) + ": " + std::to_string(num);
		}
		else if (count == 0){
			s="Case #" + std::to_string(k) + ": Volunteer cheated!";
		}
		else{
			s="Case #" + std::to_string(k) + ": Bad magician!";
		}
		output[k-1] = s;
	}
	for (int i=0; i<n; i++)
		cout<<output[i]<<endl;
	return 0;
}