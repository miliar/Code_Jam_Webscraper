#include <iostream>
#include <string>
#include <sstream>
#include <algorithm> 

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t = 1; t < T + 1; t++){
		int D;
		cin >> D;
		int list[D];
		int max = 0;
		int sp;
		int solution = 100000000;
		for(int d = 0; d < D; d++){
			cin >> list[d];
			if(list[d] > max) max = list[d];
		}
		for(int height = 1; height < max; height++){
			sp = 0;
			for(int d = 0; d < D; d++){
				sp += list[d] / height;
				if(list[d]%height == 0) sp--;
			}
			if(sp + height < solution) solution = sp + height;
		}
		if(max < solution) solution = max;
		cout << "Case #" << t << ": " << solution << "\n";
	}
}
