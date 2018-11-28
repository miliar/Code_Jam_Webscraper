#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ofstream file;
	ifstream inf;
	inf.open("A-large.in");
	file.open("output.txt");
	int T;
	inf >> T;
	
	for (int i = 1; i <= T; i++) {
		int n;
		inf >> n;
		file << "Case #" << i << ": ";
		if (n == 0) { 
			file <<"INSOMNIA" ; 
		}
		else {
			bool number[10] = { 0 };
			int cnt = 0;
			int sheep = 0;
			while (cnt != 10) {
				sheep += n;
				int x = sheep;
				while (x > 0){
					if (!number[x % 10]) {
						number[x % 10] = true;
						cnt++;
					}
					x /= 10;
				}
				
			}
			file << sheep;
		}
		file << endl;
	}
	return 0;
}