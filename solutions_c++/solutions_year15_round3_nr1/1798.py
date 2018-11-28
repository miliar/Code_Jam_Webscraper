#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;


// int cal(int r, int w, int piece){
// 	int p=0;
// 	if(r/2<=w){
// 		return 1;
// 	}else{
// 		p = p + piece*2*cal(r/2,w);
// 	}
// }


int main(){
	//ifstream fin("simple.txt");
	ifstream fin("A-small-attempt1.in.txt");
	//ifstream fin("A-large-practice.in-3.txt");
	//ofstream fout("s.txt");
	ofstream fout("small.txt");
	//ofstream fout("large.txt");
	string line;
	getline(fin, line);
	int cases = stoi(line);
	for(int i=1;i<=cases;i++){
		fout << "Case #" << i << ": ";
		int R, C, W;
		fin >> R >> C >> W;
		int n = R*ceil((double)C/W)+W-1;
		fout << n << endl;
	}
	return 0;
}