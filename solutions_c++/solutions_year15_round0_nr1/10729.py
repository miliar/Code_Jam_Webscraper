#include<iostream>
#include<string>
#include<fstream>

using namespace std;

ofstream outfile("A-small-attempt2.out");

void fileprep(int casenum, int num){
	outfile << "Case " << "#" << casenum << ": " << num << endl;
	return;
}


int main(){
	ifstream infile("A-small-attempt2.in");
	int datasize, smax, extra, clapping;
	string audlist;
	infile >> datasize;
	for (int i = 1; i <= datasize; i++){
		infile >> smax >> audlist;
		clapping = audlist.at(0)-'0';
		extra = 0;
//		cout << " clapping " << clapping << " extra: " << extra << " smax " << smax << endl;
		for(int j = 1; j <= smax; j++){
			if((clapping < j) && ((audlist.at(j) - '0') != 0)){
				extra += j - clapping;
				clapping += extra + (audlist.at(j) - '0');
//				cout << " clapping " << clapping << " extra: " << extra << " smax " << smax << endl;
				continue;
			}
			clapping += audlist.at(j) - '0';
//			cout << " clapping " << clapping << " extra: " << extra << " smax " << smax << endl;
		}
		fileprep(i, extra);
	}
}
