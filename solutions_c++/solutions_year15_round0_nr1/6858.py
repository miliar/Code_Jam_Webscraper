#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <sstream>

using namespace std;

int main(int argc, char* argv[]){
	int tests;
	ifstream ifile(argv[1]);
	ofstream ofile(argv[2]);
	ifile >> tests;
	for(int i = 0; i < tests; i++){
		int s_max; string dist;
		ifile >> s_max;
		ifile >> dist;
		vector<int> audience;
		for(int x = 0; x < dist.size(); x++){
			stringstream ss; int current;
			ss << dist[x];
			ss >> current;
			audience.push_back(current);
		}
		int min_add = 0;
		for(int j = 0; j < audience.size(); j++){
			int sum = 0;
			for(int y = 0; y < j; y++){
				sum += audience[y];
			}
			while(sum < j){
				audience[0]++;
				sum++;
				min_add++;
			}			
		}
		ofile << "Case #" << i+1 << ": " << min_add << endl;
	}
	return 0;
}