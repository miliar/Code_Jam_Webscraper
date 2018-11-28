#include <iostream>
#include <vector>
#include <string>
#include <utility>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int j = 0; j < T; j++){
		int Smax;
		string levels;
		cin >> Smax >> levels;
		vector<int> numShyness(levels.begin(), levels.end());
		//cout << numShyness[0];
		int counter = 0;
		int standing = 0;
		for(int i = 0; i < levels.size(); i++){
			if(standing < i){
				counter += i - standing;
				standing += i - standing;
			}
			standing += (levels[i]-'0');
		}
		cout << "Case #" << j+1 << ": " << counter << endl;
	}
}