#include <iostream>
#include <fstream>

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	//cout << "Hello World" << endl ;
	fstream fs;
	fs.open ("input.txt", std::fstream::in | std::fstream::out | std::fstream::app);
	int T;
	fs >> T;
	//cout << T << endl;
	return 0;
}
