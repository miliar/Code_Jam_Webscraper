#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(){
	ifstream fin ("ovation.in");
	ofstream fout ("ovation.out");

	int T; fin >> T;
	
	for(int t = 0; t < T; t++){
		int Smax; fin >> Smax;
		int toInvite = 0;
		int standing = 0;
		int audience; fin >> audience;

		for(int k = 0; k <= Smax; k++){
			int cur = audience/((int)pow(10,Smax-k))%10;
			if(standing < k){
				int curInvite = k - standing;
				toInvite += curInvite;
				standing += curInvite;
			}
			standing += cur;
		}

		fout << "Case #" << t+1 << ": " << toInvite << endl;
	}

	return 0;
}