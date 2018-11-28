#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;
struct SP {
	string st;
	string ms;
	int MS[101];
};
int main() {
	int T, N;
	ifstream fin;
	ofstream fout;
	
	fin.open("B-large.in");
	fout.open("B-large-answer.in");
	fin >> T;
	for(int mcase=1;mcase<=T;mcase++) {
		fout << "Case #" << mcase << ": ";

		fin >> N;

		bool CHECK = true;

		SP *S = new SP[101];

		for(int i=0;i<N;i++) {

			fin >> S[i].st; // 문자를 받는다. 

			for(int k=0;k<S[i].st.length();k++) { // 문자를 하나씩 확인

				if(S[i].ms == "" || S[i].ms[S[i].ms.length()-1] != S[i].st[k]) {
					S[i].ms += S[i].st[k];
					S[i].MS[S[i].ms.length()-1] = 0;
				} 
				S[i].MS[S[i].ms.length()-1]++; // 해당 글자의 출현 수를 구한다. -> 출현 수의 평균만큼만 출력하는 것이 최선
			}
			if(i > 0 && S[i].ms != S[i-1].ms) CHECK = false; // F win
		}
		if(CHECK == false) fout << "Fegla Won";
		else {
			int MST[101], L = S[0].ms.length(), res=0;
			for(int k=0;k<L;k++) {
				MST[k] = 0;
				for(int i=0;i<N;i++) {
					MST[k] += S[i].MS[k];
				}
				MST[k] /= N;
				for(int i=0;i<N;i++) {
					res += abs(MST[k]-S[i].MS[k]);
				}
			}
			fout << res;
		}
		fout << endl;
	}
	fout.close();
	return 0;
}