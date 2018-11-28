#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i=0;i<t;++i) {
		string pancakes;
		cin >> pancakes;
		int lastSorted = pancakes.length();
		int flips = 0;
		while (lastSorted > 0) {
			while(lastSorted > 0 && pancakes[lastSorted-1] == '+') {
				--lastSorted;
			}
			if (lastSorted > 0) {
				//we need to flip here. Check whether the top looks right
				if (pancakes[0] == '+') {
					++flips;
					int flippos = 0;
					while (flippos < lastSorted && pancakes[flippos] == '+') {
						pancakes[flippos] = '-';
						++flippos;
					}
				}
				++flips;
				string newTop = "";
				for (int j=0;j<lastSorted;++j){
					newTop += pancakes[j] == '+' ? '-' : '+';
				}
				for (int j=0; j<lastSorted;++j) {
					pancakes[j] = newTop[lastSorted-1-j];
				}
				while (lastSorted> 0 && pancakes[lastSorted-1] == '+') {
					--lastSorted;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << flips <<endl;
	}
}
