#include <iostream>

using namespace std;


int main(){
	ios::sync_with_stdio(false);

	int testcases;
	int oldmachine,newmachine,catalina,counter=1;
	long long result=0;

	cin >> testcases;
	while(testcases-- > 0){
		cin >> oldmachine >> newmachine >> catalina;

		for(int i = 0 ; i < oldmachine; i++){
			for(int j = 0 ; j < newmachine ; j++){
				if((i&j) < catalina)
					result++;
			}
		}

		cout << "Case #" << counter++ << ": " << result << endl; 
		result = 0;
	}
}