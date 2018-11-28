// partially solved by hand, this code will only work on my machine
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
bool winnable[21][21][21];
int main(){
	int a,b,c,d;
	ifstream fin("d.out");
	while(fin >> a >> b >> c >> d){
		winnable[a][b][c]=d;
	}
	int T;
	cin >> T;
	for(int test = 1; test <= T; ++test){
		int a,b,c;
		cin >> a >> b >> c;
		cout << "Case #" << test << ": ";
		if(!winnable[a][b][c])
			cout << "RICHARD\n";
		else
			cout << "GABRIEL\n";
	}
}
