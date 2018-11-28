#include <iostream>
#include <map>
#include <fstream>
using namespace std;
int main() {
	int T, A, B, K;
	ifstream fin;
	ofstream fout;
	
	fin.open("B-large.in");
	fout.open("B-large-answer.in");
	fin >> T;
	for(int mcase=1;mcase<=T;mcase++) {
		fout << "Case #" << mcase << ": ";

		fin >> A >> B >> K;
		map <int,int> m1;
		int cnt = 0;
		for(int a=0;a<A;a++) {
			for(int b=0;b<B;b++) {
				if((a&b) < K) cnt++;
			}
		}
		fout << cnt << endl;
	}
	fout.close();
	return 0;
}