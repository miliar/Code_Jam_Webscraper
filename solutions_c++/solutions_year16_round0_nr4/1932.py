#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream out;
	out.open("D-small-output");

	int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		int K, C, S;
		cin >> K >> C >> S;
		out << "Case #" << i << ": ";
		for(int j = 1; j <= S; j++){
			out << j << ' ';
		}
		out << '\n';
	}
	out.close();
}