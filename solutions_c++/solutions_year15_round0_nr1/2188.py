#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t = 1; t < T + 1; t++){
		int S;
		cin >> S;
		int result = 0;
		int count = 0;
		int N;
		string line;
		cin >> line;
		for(int s = 0; s < S + 1; s++){
			int N = line[s] - '0';
			if(count < s){
				result ++;
				count ++;
			}
			count += N;
			//cout << count << " ";
		}
		cout << "Case #" << t << ": " << result << "\n";
	}
}
