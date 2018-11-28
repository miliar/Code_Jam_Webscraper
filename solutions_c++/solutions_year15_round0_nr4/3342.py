#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]){

	string fin = argv[1];
	ifstream istr(fin.c_str());

	ofstream ostr(argv[2]);

	int x,r,c,t,remaining;
	bool value;

	istr >> t;

	for (int i=0;i<t;i++){

		istr >> x >> r >> c;

		if (x > 6) value = false;
		else if (x > r && x > c) value = false;
		else if (x <= r){
			if (x > (c+1)) value = false;
			else{
				remaining = (c*r) - x;
				if (remaining%x == 0) value = true;
				else value = false;
			}
		}
		else if (x <= c){
			if (x > (r+1)) value = false;
			else{
				remaining = (c*r) - x;
				if (remaining%x == 0) value = true;
				else value = false;
			}
		}
		else{
			remaining = (c*r) - x;
			if (remaining%x == 0) value = true;
			else value = false;
		}

		if (value == true) ostr << "Case #" << i+1 << ": GABRIEL" << endl;
		else ostr << "Case #" << i+1 << ": RICHARD" << endl;

	}

}