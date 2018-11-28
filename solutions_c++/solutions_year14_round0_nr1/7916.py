#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int i=0; i<T; i++){
		int A, B;
		cin>>A;
		int x1,x2,x3,x4;
		vector<int> b1, b2;
		for(int j=0; j<4; j++){
			cin>>x1>>x2>>x3>>x4;
			if(j == A-1){
				b1.push_back(x1);
				b1.push_back(x2);
				b1.push_back(x3);
				b1.push_back(x4);
			}
		}
		
		cin>>B;
		for(int j=0; j<4; j++){
			cin>>x1>>x2>>x3>>x4;
			if(j == B-1){
				b2.push_back(x1);
				b2.push_back(x2);
				b2.push_back(x3);
				b2.push_back(x4);
			}
		}
		
		int counter = 0;
		int found = -1;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				if(b1[j] == b2[k]){
					counter++;
					found = b1[j];
					break;
				}
			}
		}
		
		cout<<"Case #"<<i+1<<": ";
		if(counter == 0){
			cout<<"Volunteer cheated!";
		} else{
			if(counter == 1){
				cout<<found;
			} else{
				cout<<"Bad magician!";
			}
		}
		cout<<endl;
	}
	return 0;
}