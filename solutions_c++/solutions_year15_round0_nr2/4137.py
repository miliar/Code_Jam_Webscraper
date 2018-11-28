#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main(){
	ifstream fin("pancake.in"); ofstream fout("pancake.out");

	int T; int c[1001];
	fin >> T;
	for(int i = 1; i <= T; ++i){
		memset(c, 0, sizeof(c));
		int a, b;
		fin >> a;
		for(int i = 0; i < a; ++i){
			fin >> b;
			++c[b];
		}
		
	}
	return 0;
}
