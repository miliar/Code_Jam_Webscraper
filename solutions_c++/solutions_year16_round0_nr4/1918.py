#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int main(){
	ifstream fin("test.in");
	ofstream fout("test.out");
	int T;
	fin >> T;
	for (int i=1;i<T+1;i++){
		int K, C, S;
		fin >> K >> C >> S;
		fout << "Case #" << i << ":";
		if (K>S)fout << " IMPOSSIBLE";
		else{
			long long temp=0;
			for(int j=0;j<C;j++){
				long long EXP=1;
				for (int k=0;k<j;k++){
					EXP=EXP*K;
				}
				temp+=EXP;
			}
			for(int j=0;j<S;j++){
				fout << " " << (temp*j)+1;
			}
		}
		fout << endl;
	}
	system("pause");
}