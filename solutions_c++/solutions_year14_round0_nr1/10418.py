#include "iostream"

using namespace std;

int main() {
	int N;
	cin >> N;
	int r1, r2; 
	int a1[4], a2[4];
	for(int j = 0; j<N; j++) {
		cin >> r1;
		for(int i=0; i<16;i++) {
			int temp;
			cin>> temp;
			if(i/4 +1==r1) {
				a1[i%4] = temp;
			}

		}
		cin>>r2;
		for(int i=0; i<16;i++) {
			int temp;
			cin>> temp;
			if(i/4 +1==r2) {
				a2[i%4] = temp;
			}

		}
		
		int count  = 0;
		int val;
		for(int i=0; i<4; i++){
			for(int k = 0; k<4; k++) {
				if(a1[i]==a2[k]){
					val = a1[i];
					count++;
				}
			}
		}
		if(count ==0)
		cout<<"Case #"<<j+1<<": "<<"Volunteer cheated!\n";
		else if(count ==1) 
		cout<<"Case #"<<j+1<<": "<<val<<"\n";
		else
		cout<<"Case #"<<j+1<<": "<<"Bad magician!\n";
	}
}
