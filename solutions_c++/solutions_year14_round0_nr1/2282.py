#include <iostream>
#include <fstream>

using namespace std;

int main() {
	fstream fin("A-small-attempt1.in",ios::in);
	fstream fout("A-small-attempt1.out",ios::out);
	int T;
	fin>>T;
	int i;
	for(i = 1;i <= T;i++) {
		int a1, a2;
		int temp, correctRow[4];
		int answer = -1, count = 0;
		fin>>a1;
		int j;
		for(j = 1;j <= (a1-1)*4;j++) {
			fin>>temp;
		}
		for(j = 0;j < 4;j++) {
			fin>>correctRow[j];
		}
		for(j = 0;j < (4-a1)*4;j++) {
			fin>>temp;
		}

		fin>>a2;
		for(j = 1;j <= (a2-1)*4;j++) {
			fin>>temp;
		}
		for(j = 0;j < 4;j++) {
			int tmpans;
			fin>>tmpans;
			int k;
			for(k = 0;k < 4;k++) {
				if(tmpans == correctRow[k]) {
					answer = tmpans;
					count++;
					break;
				}
			}
		}
		for(j = 0;j < (4-a2)*4;j++) {
			fin>>temp;
		}

		if(count == 0) {
			fout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
		else if(count == 1) {
			fout<<"Case #"<<i<<": "<<answer<<endl;
		}
		else {
			fout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
	}

	return 0;
}