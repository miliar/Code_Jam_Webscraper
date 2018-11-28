#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin  ("pancake.in");
ofstream fout ("pancake.out");

int num_upright(string S){
	int count = 0;

	for(string::reverse_iterator rit = S.rbegin(); rit != S.rend(); rit++){
		if(*rit == '+'){
			count++;
		}
		else{
			break;
		}
	}

	return count;
}

string flip(string S, int i){
	string res = S;

	for(string::iterator it = res.begin(); it != res.begin()+i+1; it++){
		*it = (*it == '+') ? '-' : '+';
	}

	return res;
}

int main(){
	unsigned int T;
	string S;

	fin >> T;

	for(int t = 0; t < T; t++){
		fin >> S;

		int flips = 0;

		while(num_upright(S) != S.length()){
			S = flip(S, S.rfind("-"));
			flips++;
		}

		fout << "Case #" << t+1 << ": " << flips << endl;
	}

	return 0;
}