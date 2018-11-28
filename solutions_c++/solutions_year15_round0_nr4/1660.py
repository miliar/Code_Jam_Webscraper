#include <iostream>
#include <fstream>

int max(int a, int b){
	if(a > b)
		return a;
	else 
		return b;
}

int min(int a, int b){
	if(a < b)
		return a;
	else 
		return b;
}

using namespace std;

int main(){
	//ifstream fin("B-large.in.txt");
	ifstream fin("D-small-attempt2.in.txt");
	ofstream fout("small.txt");
	//ofstream fout("large.txt");
	//ofstream fout("s.txt");
	string line;
	getline(fin, line);
	int cases = stoi(line);
	for(int i=1;i<=cases;i++){
		fout << "Case #" << i <<": ";
		int X, R, C;
		fin >> X >> R >> C;
		string winner;
		if (R*C%X!=0)
			winner = "RICHARD";
		else if (X>min(R,C)+1)
			winner = "RICHARD";
		else 
			winner = "GABRIEL";
		// if(X==1&&R==1&&C==1)
		// 	winner = "GABRIEL";
		// else if(R*C%X!=0)
		// 	winner = "RICHARD";
		// else if( X >  max(R,C))
		// 	winner = "RICHARD";
		// else if (X>=2*min(R,C)+1){
		// 	winner = "RICHARD";
		// }else if (X>=R+C-1 && R!=1 && C!=1){
		// 	winner = "RICHARD";
		// }else if (X>=min(R,C)+2){
		// 	winner = "RICHARD";
		// }else
		// 	winner = "GABRIEL";

		fout << winner << endl;

	}

	return 0;
}


