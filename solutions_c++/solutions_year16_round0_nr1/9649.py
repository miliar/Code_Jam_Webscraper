#include <iostream>
using namespace std;

int main() {
	int T, N;
	int x, y;
	bool seen[10];
	bool done;
	
	cin >> T;
	
	for(int i = 0; i < T; i++){
		cin >> N;
		if(N == 0){
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		
		for(int j = 0; j < 10; j++){
			seen[j] = false;
		}
		done = false;
		y = N;
		
		while(!done){
			x = y;
			while(x != 0){
				seen[x % 10] = true;
				x = x/10;
			}
			
			done = true;
			for(int j = 0; j < 10; j++){
				done = done && seen[j];
			}
			
			if(done){
				cout << "Case #" << i+1 << ": " << y << endl;
			}
			else{
				y = y + N;
			}
		}
	}
	
	return 0;
}