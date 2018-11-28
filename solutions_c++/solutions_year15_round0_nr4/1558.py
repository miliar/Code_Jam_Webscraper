#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char* argv[]){
	int T;

	ifstream ifs("D-small-attempt0.in", ifstream::in);
	ofstream ofs("D-small-attempt0.out");
	
	ifs >> T; //  # test cases
	for(int it = 0; it<T; it++)
	{
		// input
		int X = 0;
		int R = 0;
		int C = 0;
		ifs >> X >> R >> C;
		
		// output
		if(X == 1){
			ofs << "Case #" << it+1 << ": " << "GABRIEL" << endl;
			continue;
		}
		if((R*C)%X>0 || (X>2 && max(R,C)<X) || (X>2 && R*C==X)){
			ofs << "Case #" << it+1 << ": " << "RICHARD" << endl;
			continue;
		}
		if(X==4 && R*C==8){
			ofs << "Case #" << it+1 << ": " << "RICHARD" << endl;
			continue;
		}
		
		ofs << "Case #" << it+1 << ": " << "GABRIEL" << endl;
	}
	ifs.close();
	ofs.close();
	return 0;
}