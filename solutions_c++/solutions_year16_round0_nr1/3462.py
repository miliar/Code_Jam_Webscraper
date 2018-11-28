#include <iostream>
#include <cstdio>

using namespace std;

void digitsin(int x, int arr[]){
	int n = x;
	while(n != 0){
		// cout << "n = " << n << endl;
		int d = n%10;
		arr[d] = 1;
		n=n/10;		
	}
}

int main(){
	int T;
	// cout << "Enter T: ";
	cin >> T;
	int arr[10];
	for(int t=1;t<=T;t++){
		int i;
		// cout << "Enter N: ";
		cin >> i;
		if(i==0) cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		else {
			for(int j=0;j<10;j++) arr[j] = 0;
			//cout << "1\n";
			int j=1;
			while(1){
				int temp[10];
				for(int k=0;k<10;k++){
					temp[k] = 0;
				}
				digitsin(j*i, temp);
				// cout << "2\n";
				for(int k=0;k<10;k++){
					if(temp[k]==1) arr[k]=1;
				}
				int count=0;
				for(int k=0;k<10;k++) count+=arr[k];
				if(count==10){
					cout << "Case #" << t << ": " << j*i << endl;
					break;
				}
				j++;
			}
		}
	}
	return 0;
}