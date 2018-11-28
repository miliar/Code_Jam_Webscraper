#include <iostream>
using namespace std;

int main(){

int t;

cin >> t;

for(int i = 0; i < t; i++){
	
	unsigned long long int n;
	cin >> n;
	
	if(n == 0){
		cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		continue;
	}

	int digitArray[10] = {0};

	for(int j = 1; true; j++){
		unsigned long long int multiple = n * j;
		unsigned long long int multipleCopy = multiple;
		bool success = true;
		
		while(multiple > 0){
			digitArray[multiple % 10] = 1;
			multiple /= 10;
		}

		for(int j = 0; j < 10; j++){
			if(digitArray[j] == 0)
				success = false;
		}

		if(success){
			cout << "Case #" << i + 1 << ": " << multipleCopy << endl;
			break;
		}	

	}
}

return 0;

}
