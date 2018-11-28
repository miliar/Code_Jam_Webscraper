#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;
int T = 0;
int N = 0;
void solve(int X, int R, int C,int T) {
	ofstream outFile;
	outFile.open("result.txt",ios::app);
	if((R*C) % X != 0) {
		outFile<<"Case #"<<(N-T)<<": "<<"RICHARD"<<endl;
	}else if(X == 1) {
		outFile<<"Case #"<<(N-T)<<": "<<"GABRIEL"<<endl;
	}else if(X == 2) {
		outFile<<"Case #"<<(N-T)<<": "<<"GABRIEL"<<endl;
	}else if(X == 3) {
		if(C == 1 || R == 1) {
			outFile<<"Case #"<<(N-T)<<": "<<"RICHARD"<<endl;
		}else {
			outFile<<"Case #"<<(N-T)<<": "<<"GABRIEL"<<endl;
		}
	}else if(X == 4){
		if(C <= 2 || R <= 2)
			outFile<<"Case #"<<(N-T)<<": "<<"RICHARD"<<endl;
		else
			outFile<<"Case #"<<(N-T)<<": "<<"GABRIEL"<<endl;
	}
	outFile.close();
}

int main() {
	cin >>T;
	N = T;
	int X,R,C;
	while(T--) {
		cin>>X>>R>>C;
		solve(X,R,C,T);
	}
}

