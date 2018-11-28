#include<fstream>
#include<string>
#define DINERMAX 1010
#define PANCAKEMAX 1010
using namespace std; 

int main(void){
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in", ios_base::in);
	fout.open("B-large.out", ios_base::trunc);
	int T;
	fin >> T;
	for(int c = 1; c <= T; c++){
		int dinerCount = 0;
		int pancake[DINERMAX];
		fin >> dinerCount;
		for(int i = 0; i < dinerCount; i++)
			fin >> pancake[i];
		
		int minuteMax = 0;
		for(int i = 0; i < dinerCount; i++){
			if(minuteMax < pancake[i])
				minuteMax = pancake[i];
		}
		int optMinute = minuteMax;
		for(int bar = 1; bar < minuteMax; bar++){
			int m = 0;
			for(int d = 0; d < dinerCount; d++){
				if(pancake[d] > bar){
					m += (pancake[d] + bar - 1) / bar - 1;
				}
			}
			if(optMinute > bar + m)
				optMinute = bar + m;
		} 

		//output
		fout << "Case #" << c << ": " << optMinute << endl;
	}
	return 0;
}
