#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
using namespace std;
int katefirst(vector<int> d){
	int sum = 0;
	for (int i = 0; i < d.size()-1; i++){
		if (d[i] > d[i + 1]){
			sum += d[i] - d[i + 1];
		}
	}

	return sum; 
}
int katesecond(vector<int> d){
	double speed = 0;
	double sum = 0;
	for (int i = 0; i < d.size() - 1; i++){
		if (d[i] > d[i + 1]){
			double temp = ((double)d[i] - (double)d[i + 1]) / 10;
			speed = max(speed, temp);
		}
	}
	cout << speed << endl;
	for (int i = 0; i < d.size()-1; i++){
		sum += min(10 * speed, (double)d[i]);
	}
	
	return (int)sum;
}

void main() {
	
	ifstream q;
	q.open("C:\\Users\\songr_000\\Desktop\\A-large.in");
	ofstream ofs("C:\\Users\\songr_000\\Desktop\\output.txt");

	int T;
	q >> T;
	for (int i = 1; i <= T; i++){
		int N; 
		q >> N;
		vector<int> d;
		for (int j = 0; j < N; j++){
			int temp; 
			q >> temp;
		
			d.push_back(temp);
		}
		
		ofs << "Case #" << i << ": " << katefirst(d) << " " << katesecond(d) << endl;
	}
	
		//ofs << "Case #" << i << ": " << stuff << endl;
	
	ofs.close();



}


