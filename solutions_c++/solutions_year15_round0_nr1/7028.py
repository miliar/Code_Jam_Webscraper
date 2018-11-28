#include <bits/stdc++.h>

using namespace std;

int main(){
	ofstream outputFile;
	outputFile.open("output.out");
	cin.tie();
	int T;
	cin >> T;
	for (int i = 0; i < T; i++){
		int a;
		string s;
		cin >> a >> s;
		int pos = 0;
		int tmp = 0;
		int orang = 0;
		while(pos<=s.length()-1){
			int temp = s[pos] - '0';
			if (tmp >= pos){
				tmp += temp;
			}
			else if (tmp < pos){
				orang += pos-tmp;
				tmp = pos + temp;
			}
			pos++;
		}
		outputFile << "Case #" << i+1 << ": " << orang << '\n';
	}
	outputFile.close();
}
