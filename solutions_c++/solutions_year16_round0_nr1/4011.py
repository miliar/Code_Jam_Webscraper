#include <fstream>

using namespace std;

ifstream fin  ("sheep.in");
ofstream fout ("sheep.out");

bool seen [10] = {false};

bool all_seen(){
	for(int k = 0; k < 10; k++){
		if(seen[k] == false){
			return false;
		}
	}
	return true;
}

void reset(){
	for(int k = 0; k < 10; k++){
		seen[k] = false;
	}
}

int main(){
	unsigned int T;
	unsigned long long N;

	fin >> T;

	for(int t = 0; t < T; t++){
		reset();
		fin >> N;

		if(N == 0){
			fout << "Case #" << t+1 << ": " << "INSOMNIA" << endl;
			continue;
		}

		int k = 0;
		while(all_seen() == false){
			k++;
			int n = k*N;
			while(n > 0){
				seen[n%10] = true;
				n /= 10;
			}
		}

		fout << "Case #" << t+1 << ": " << k*N << endl;
	}

	return 0;
}