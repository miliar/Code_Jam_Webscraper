//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <time.h>
//#include <cstdlib>

using namespace std;

template<typename T>
void print(const vector<vector<T>> &tb){
	for (int i=0; i!=tb.size(); ++i){
		vector<T> row = tb[i];
		for (int j=0; j!=row.size(); ++j)
			cout<<row[j]<<" ";
		cout<<endl;
	}
}

template<typename T>
void print(const vector<T> &a){
	for (int j=0; j!=a.size(); ++j)
		cout<<a[j]<<" ";
	cout<<endl;
}

int main() {
	//generate my own test sample 
	/*
	clock_t t1 = clock();
	FILE * pFile = fopen("test.txt", "w");
	int T=50;
	fprintf(pFile, "%d\n", T);
	for(int t=0; t!=T; t++){
		int N=rand()%1000;
		fprintf(pFile, "%d\n", N);
		double r;
		for(int j=0; j!=2; j++){
			for(int n=0; n<N-1; n++){
				r = ((double) rand() / RAND_MAX) ;
				fprintf(pFile, "%.5f ", r);
			}
			r = ((double) rand() / RAND_MAX) ;
			fprintf(pFile, "%.5f\n", r);
		}
	}
	fclose(pFile);
	*/
	
	clock_t t1 = clock();
	//ifstream infile("testsmall.txt");
    //ifstream infile("D-small-attempt0.in");
	//ofstream outfile("D.out");
	ifstream infile("D-large.in");
	ofstream outfile("Dlarge.out");
	
	string instr;
	getline(infile, instr);
	int T = stoi(instr);
	cout<<T<<endl;

	for(int t=0; t!=T; t++){
		getline(infile, instr);
		int N = stoi(instr);

		vector<double> Naomi(N, 0);
		vector<double> Ken(N, 0);

		getline(infile, instr);
		stringstream sstr = stringstream(instr);
		string item;
		for(int i=0; i!=N; i++){
			getline(sstr, item, ' ');
			stringstream(item)>>Naomi[i];
		}

		getline(infile, instr);
		sstr = stringstream(instr);
		for(int i=0; i!=N; i++){
			getline(sstr, item, ' ');
			stringstream(item)>>Ken[i];
		}
		
		//print(Naomi); print(Ken);
		sort(Naomi.begin(), Naomi.end());//sort in increasing order
		sort(Ken.begin(), Ken.end());
		//print(Naomi); print(Ken);

		int optWin = N, decWin = 0;
		int iN = 0, iK=0, iKst = 0;
		while(iN<N){
			while(iN<N && Naomi[iN]<Ken[iK]){
				iN++;
			}
			if(iN<N){
				decWin++;
				iN++; iK++;
			}
		}
		//cout<<"deceitful optimal play win: "<<decWin<<endl;
		for(iN=0; iN<N; iN++){
			for(iK = iKst; iK<N; iK++){
				if(Ken[iK] > Naomi[iN]){
					optWin--;
					iKst = iK+1;
					break;
				}
			}
			if(iK==N)
				break;
		}
		//cout<<"optimal play win: "<<optWin<<endl;
		outfile<<"Case #"<<t+1<<": "<<decWin<<" "<<optWin<<endl;	
	}
	infile.close();
	outfile.close();
	
	clock_t t2 = clock();
	cout<<"Total time used "<<(t2-t1)/CLOCKS_PER_SEC<<"s"<<endl;
	cin.get();
    return 0;
}
