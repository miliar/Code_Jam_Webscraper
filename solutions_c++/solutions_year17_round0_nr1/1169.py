#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


void flip(string& str, size_t index, size_t size){
    for (size_t i = index; i < index+size; ++i){
		if (str[i] == '+') str[i] = '-';
		else str[i] = '+';
	}
}

int main( int argc, char** argv){
	size_t cnt;
	vector<string> cakerow;
	vector<size_t> flipsize;
	ifstream ip("input.txt");
	ip >> cnt;
	cakerow.resize(cnt);
	flipsize.resize(cnt);
	for (size_t i = 0; i < cnt; ++i)
		ip >> cakerow[i] >> flipsize[i];
	ip.close();
	vector<size_t> result(cnt,0);
	for (size_t cas = 0; cas < cnt; ++cas){
		size_t i;
		for (i = 0; i < cakerow[cas].size()+1-flipsize[cas]; ++i){
			if (cakerow[cas][i]=='-'){
				++result[cas];
                flip(cakerow[cas],i,flipsize[cas]);
			}
		}
		for (; i < cakerow[cas].size(); ++i){
			if (cakerow[cas][i]=='-'){
				result[cas]=-1;
				break;
			}
		}
	}
	ofstream op("output.txt");
	for (size_t i = 0 ; i<cnt; ++i){
		op << "Case #" << i+1 <<": ";
		if (result[i] != -1) op << result[i];
		else op << "IMPOSSIBLE"; 
		op << endl;
	}
	op.close();
	return 0;
}
