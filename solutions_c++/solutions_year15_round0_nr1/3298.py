#include<fstream>
#include<string>
#define SMAX 1010
using namespace std;

int main(void){
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in", ios_base::in);
	fout.open("A-large.out", ios_base::trunc);
	int T;
	fin >> T;
	for(int c = 1; c <= T; c++){
		int shynessMax = 0;
		string audienceCount = "";
		fin >> shynessMax >> audienceCount;
		
		int audience[SMAX];
		int dist[SMAX];
		for(int shyness = 0; shyness <= shynessMax; shyness++){
			audience[shyness] = audienceCount[shyness] - '0';
		}
		
		int audienceTotal = 0;
		dist[0] = 0;
		for(int shyness = 1; shyness <= shynessMax; shyness++){
			audienceTotal += audience[shyness - 1];
			dist[shyness] = shyness - audienceTotal;
		}
		
		int friendCount = 0;
		for(int shyness = 0; shyness <= shynessMax; shyness++){
			if(friendCount < dist[shyness])
				friendCount = dist[shyness];
		}
		
		//output
		fout << "Case #" << c << ": " << friendCount << endl;
	}
	return 0;
}
