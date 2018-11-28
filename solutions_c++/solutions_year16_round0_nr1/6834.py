#include<iostream>
#include<fstream>

using namespace std;

int main() {
	ifstream open;
	fstream out;
	open.open("A-large.in");
	out.open("output", ios::out);
	
	if (!open.is_open()) {
		return 1;
	}

	int Text,N;
	open >> Text;
	
	
	for (int cases = 1; cases <= Text; cases++) {
		out << "Case #" << cases << ": ";
		open >> N;
		int ans = 0;
		
		if (N == 0){ 
			out << "INSOMNIA" << endl;
			continue;
		}
		
		for (int i = 1; ans!= 1023; i++) {
			for (int temp = i*N; temp != 0; temp /= 10) {	
				ans |= 1<< (temp % 10);
				
				if (ans == 1023) {
					out << i*N << endl;
					break;
				}
				
			}
		}
	}
	
	open.close();
	return 0;
}
