#include<iostream>
#include<cstdlib>
#include<fstream>
#include<cmath>

using namespace std;

int main(){
	ifstream f1;
	f1.open("input.txt");
	ofstream f2;
	f2.open("output.txt");

	int T;
	f1 >> T;

	int X,R,C;


	for(int i=0;i<T;++i){
		f1 >> X >> R >> C;
		int maxA = max(R,C);
		int minA = min(R,C);

		//bool b = minA>1 && minA == (X+1)/2 && maxA <= ceil((X+1)/2)+1;
		bool b = X == 4 && minA==2 && maxA == 4;

		if((R*C)%X!=0 || maxA<X || minA < (X+1)/2 || b){
			f2 << "Case #" << i+1  << ": RICHARD"  << "\n";
		}else{
			f2 << "Case #" << i+1  <<": GABRIEL"  << "\n";
		}
	}

	f1.close();
	f2.close();

	return 0;
}
