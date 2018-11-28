#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

void pBlocks(int N, vector< double > &block, vector< bool > &flag){
	for(int i=0; i<N; i++){
		if(flag[i]) cout << block[i] << "\t";
	}
	cout << endl;
}

double chosenNaomi(int N, vector< double > &block, vector<bool> &flag){
	for(int i=0; i<N; i++){
		if(flag[i]){
			flag[i] = false;
			return block[i];
		}
	}
	return -1;
}

double toldNaomi(int N, vector< double > &block, vector<bool> &flag, double chosenNaomi){
	for(int i=0; i<N; i++){
		if(flag[i]){
			if(chosenNaomi > block[i]){
				return 1.0;
			}
			break;
		}
	}
	for(int i=N-1; i>=0; i--){
		if(flag[i]){
			if(chosenNaomi < block[i]){
				return block[i] - 1e-6;
			}else{
				return chosenNaomi;
			}
		}
	}
	return -1;
}

double chosenKen(int N, vector< double > &block, vector<bool> &flag, double chosenNaomi){
	for(int i=0; i<N; i++){
		if(flag[i] && (block[i] > chosenNaomi) ){
			flag[i] = false;
			return block[i];
		}
	}
	for(int i=0; i<N; i++){
		if(flag[i]){
			flag[i] = false;
			return block[i];
		}
	}
	return -1;
}

int War(int N, vector< double > &blockN, vector< double > &blockK){
	vector< bool > flagN(N, true);
	vector< bool > flagK(N, true);
	int count=0;
	for(int i=0; i<N; i++){
		double chosenN;
		double chosenK;
		
		chosenN = chosenNaomi(N, blockN, flagN);
		chosenK = chosenKen(N, blockK, flagK, chosenN);

		if(chosenN > chosenK) count++;
	}
	return count;
}

int DeceitfulWar(int N, vector< double > &blockN, vector< double > &blockK){
	vector< bool > flagN(N, true);
	vector< bool > flagK(N, true);
	int count=0;
	for(int i=0; i<N; i++){
		double chosenN;
		double toldN;
		double chosenK;

		//pBlocks(N, blockN, flagN);
		//pBlocks(N, blockK, flagK);
		
		chosenN = chosenNaomi(N, blockN, flagN);
		toldN = toldNaomi(N, blockK, flagK, chosenN);
		chosenK = chosenKen(N, blockK, flagK, toldN);

		//cout <<"chosenN,toldN,chosenK : " <<  chosenN << "," << toldN<< "," << chosenK <<endl;
		
		if(chosenN > chosenK) count++;
	}
	return count;
}

int main(int argc, char *argv[]){
	int T;
	
	ifstream inputfile(argv[1]);
	ofstream outputfile("output.txt");

	inputfile >> T;
	
	for(int i=0; i<T; i++){
		int N;
		inputfile >> N;
		vector<double> blockN(N);
		vector<double> blockK(N);
		for(int j=0; j<N; j++){
			inputfile >> blockN[j];
		}
		sort(blockN.begin(), blockN.end());
		for(int j=0; j<N; j++){
			inputfile >> blockK[j];
		}
		sort(blockK.begin(), blockK.end());
		int x = DeceitfulWar(N, blockN, blockK);
		int y = War(N, blockN, blockK);
		
		cout << "Case #" << i+1 << ": " << x << " " << y << endl;
		outputfile << "Case #" << i+1 << ": " << x << " " << y << endl;
	}
	return 0;
}