#include <iostream>
#include <fstream>
using namespace std;
int main(){
	ifstream infile;
	infile.open("input.in",ios::in);
	ofstream outfile;
	outfile.open("output.txt",ios::out);
	int t;
	infile >> t;
	for(int p = 1; p <= t; p++){
		string S;
		infile >> S;
		outfile << "Case #" << p << ": ";
		int ans = 0;
		int l = S.length();
		int x = l - 1;
		if(S[x] == '-')
			ans++;
		x--;
		for( ; x >= 0; x--){
			if(S[x] != S[x+1])
				ans++;
		}
		outfile << ans << endl;
	}
	return 0;
}
