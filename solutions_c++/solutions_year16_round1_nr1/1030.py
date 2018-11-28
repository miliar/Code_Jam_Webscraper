#include <iostream>
using namespace std;

int main(){
	
	int z;
	cin >> z;
	
	for(int p = 1; p <= z; p++){
		string X;
		cin >> X;
		
		string H = "";
		H = H + X[0];
		
		for(int i = 1; i < (int)X.size(); i++){
			if(X[i] >= H[0]){
				H = X[i] + H;
			}else{
				H = H + X[i];
			}
		}
		
		cout << "Case #"<< p << ": " <<H << endl;
	}
	
	return 0;
}
