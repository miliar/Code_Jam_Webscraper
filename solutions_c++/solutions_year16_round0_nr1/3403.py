#include <iostream>
using namespace std;

int T;
int check[11];
int found;

int update(int x){
	//cout << "x is " << x << "\n";
	int y = x;
	
	while(y!=0){
		//cout << "y is " << y << "and y%10 is " << y%10 << "\n";
		check[y%10]=1;
		y/=10;
	}
	
	int k = 0;
	for(int a = 0; a<=9; a++) {
		//cout << "Check " << a << " is " << check[a] << "\n";
		if(check[a]==0) k = 1;
		//cout << "k is " << k;
	}
	
	//If k == 1 means that still need to continue because it's not filled yet
	if(k==0){
		found=1;
		//cout << "FOUND! " << found << "\n";
		cout << x <<"\n";
	}
	
	
}

int main(){
	
	cin >> T;
	for (int i = 1; i<=T; i++){
		int N;
		cin >> N;
		for(int j=0; j<=10; j++) check[j] = 0;
		int curr = 0;
		found = 0;
		
		cout << "Case #" << i << ": ";
		
		for(int j = 1; j<=1000; j++){
			curr += N;
			//cout << "curr is " << curr << "\n";
			update(curr);
			if (found == 1) break;
		}
		
		if (found == 0) cout << "INSOMNIA\n";
	}
}
