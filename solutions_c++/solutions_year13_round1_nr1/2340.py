#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
	ofstream out("bull.out");
	ifstream in("bull.in");
	
	int T;
	in >> T;
	
	for(int q = 0; q < T; q++){
		int r, t;
		in >> r >> t;
		int i;
		int sum = 0;
		for(i=1;;i++){
			sum += 2*r+1 + 2*2*(i-1);
			if(sum > t)
				break;
		}
		out << "Case #" << q+1 << ": " << i-1 << endl;
	}
	
	return 0;
}

