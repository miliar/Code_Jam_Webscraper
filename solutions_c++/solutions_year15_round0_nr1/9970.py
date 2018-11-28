#include <iostream>
#include <string>

using namespace std;

int main() {

	int N;
	cin >> N;
	for(int c = 0; c < N; c++){
		
		int S; cin >> S;
		string line; cin >> line;
		int sum = 0; int count = 0;
		for(int i = 0; i < line.length(); i++){
			int next = (int)line[i] - 48; 
			if(sum >= i){
				sum += next;
				continue;
			}
			else{
				count += i-sum;
				sum += next + i - sum;
				continue;
			}
		}

		cout << "Case #" << c+1 << ": " << count << endl;
	}



	return 0;
}