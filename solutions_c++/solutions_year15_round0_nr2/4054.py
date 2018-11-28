#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <fstream>
#include <cstdlib>
#include <cstring>
using namespace std;
vector<int> pan;
ofstream out2("debug");
int minute(int maxP){
	if(maxP == 0) return 0;
	//cout << maxP << endl;
	vector<int> backup = pan;
	for(int i = 0; i <= maxP; i++){
		pan[i] = pan[i+1];					
	}
	int val = minute(maxP-1);
	pan = backup;	
	int val2 = 999999999;
	for(int tMax = 1; tMax <= maxP/2; tMax++){
		pan[tMax] += pan[maxP];
		pan[maxP - tMax] += pan[maxP];
		int backP = pan[maxP];
		pan[maxP] = 0;
		int cnt = 0;
		while(pan[maxP-cnt] == 0 && (maxP-cnt) > 0){
			cnt++;
		}
		val2 = min(val2, minute(maxP-cnt) + backP - 1);
		pan[maxP] = backP;
		pan[tMax]-=backP;
		pan[maxP - tMax]-=backP;
	}
	//out2 << "PMAX: " << maxP << " VAL: " << val << " VAL2: " << val2 << endl;
	return 1+min(val, val2);
}

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");
//	int scelta;
	//cin >> scelta;
	int t;
	in >> t;
	for(int k = 1; k <= t; k++){
		
		pan.clear();
		pan.reserve(1002);
		pan.resize(1002);
		int p;
		in >> p;
		int maxP = 0;
		for(int i = 0; i < p; i++){
			int temp;
			in >> temp;
			pan[temp]++;
			maxP = max(maxP, temp);
		}
		//if(k != scelta) continue;
		out << "Case #" << k << ": " << (minute(maxP)) << endl;
		out2 << "_________________________________________________________________________________" << endl;
	}
	return 0;
}
