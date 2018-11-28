#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Pancakes {
  private:
	bool* cakes;
	int num;
  public:
	//flip cakes from top, to position pos
	void flipCakes(int pos) {
		bool* tmp = new bool[pos];
		for(int i = 0; i < pos; i++) {
			tmp[i] = !cakes[pos-i-1];
		}
		for(int i = 0; i < pos; i++) {
			cakes[i] = tmp[i];
		}
		delete[] tmp;
	}
	bool checkCakes(void) {
		for(int i = 0; i < num; i++) {
			if(cakes[i] == false)
				return false;
		}
		return true;
	}
	void printCakes(void) {
		for(int i = 0; i < num; i++) {
			cout << (cakes[i] ? '+' : '-');
		}
		cout << endl;
	}
	int runCase(void) {
		int flips = 0;
		bool top;
		bool finished = checkCakes();
		while(!finished) {
			top = cakes[0];
			int i = 1;
			for(; i < num; i++) {
				if(cakes[i] != top) {
					flipCakes(i);
					flips++;
					break;
				}
			}
			if(i == num) {
				flipCakes(num);
				flips++;
			}
			finished = checkCakes();
			//cout << "FLIP " << flips << ": ";
			//printCakes();
		}
		return flips;
	}
	Pancakes(string scakes) {
		int l = scakes.length();
		num = l;
		cakes = new bool[l];
		for(int i = 0; i < l; i++) {
			if(scakes[i] == '+')
				cakes[i] = true;
			else if(scakes[i] == '-')
				cakes[i] = false;
		}
	}
	~Pancakes(void) {
		delete[] cakes;
	}
};
int main(void) {
	int cases, cres;
	string line;
	cin >> cases;
	for(int i = 0; i < cases; i++) {
		cin >> line;
		Pancakes p(line);
		cout << "Case #" << i+1 << ": " << p.runCase() << endl;
	}
}