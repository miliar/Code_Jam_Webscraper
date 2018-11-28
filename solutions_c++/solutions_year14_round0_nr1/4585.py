#include<iostream>
using namespace std;

int count[17] = {0};
int arr[4][4] = {0};

int main(){

	int t;
	cin>>t;
	int test = 1;
	while(t--){
		for(int i=0; i<=17; i++){
			count[i] = 0;
		}
		cout<<"Case #"<<test<<": ";
		test++;
		int r1;
		cin>>r1;
		r1--;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin>>arr[i][j];
				if(i==r1){
					count[arr[i][j]]++;
				}
			}
		}
		int r2;
		cin>>r2;
		r2--;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin>>arr[i][j];
				if(i==r2){
					count[arr[i][j]]++;
				}
			}
		}

		int count2 = 0;
		int num = -1;
		for(int i=1; i<=16; i++){
			if(count[i] == 2){
				count2++;
				num = i;
			}
		}
		if(count2 == 1){
			cout<<num<<endl;
		}
		if(count2 > 1){
			cout<<"Bad magician!"<<endl;
		}
		if(count2 <= 0 ){
			cout<<"Volunteer cheated!"<<endl;
		}
		
	}


}
