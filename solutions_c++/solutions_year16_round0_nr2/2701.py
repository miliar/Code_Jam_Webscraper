#include <iostream>
#include <string>

using namespace std;

bool isPlus(char c);

int main() {
	
	int ii, cases;
	
	cin >> cases;
	
	for(ii=0; ii < cases; ii++) {
		
		string cakes;
		cin >> cakes;
		
		int answer = 0;
		bool positiveStreak = isPlus(cakes[0]);
		
		for(int i = 1; i < cakes.length(); i++) {
			
			bool thisCake = isPlus(cakes[i]);
			
			// If we're on a positive streak and this cake is negative,
			// We have to flip all before this cake
			if(positiveStreak && !thisCake || !positiveStreak && thisCake) {
				answer++;
				positiveStreak = !positiveStreak;
			}
		}
		
		// Finally, if the whole stack is now negative, flip the whole stack.
		if(!positiveStreak) answer++;
		
		cout << "Case #" << ii+1 << ": " << answer << endl;
		
	}
	
	return 0;
}

bool isPlus(char c) {
	return (c == '+');
}
