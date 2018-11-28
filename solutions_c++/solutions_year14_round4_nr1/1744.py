#include <iostream> 
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
using namespace std;

void fn();

int
main(){
	int nTest; 

	cin >> nTest;

	for(int i = 1; i <= nTest; i++){
		cout << "Case #" << i << ": ";
		fn();
	}

	return 0;
}

void bubbleSort(vector<int> & v){
	int i = v.size();
	bool sorted = false;
	while(!sorted && i > 0){
		sorted = true; 
 
		for(int j = 0; j < i - 1; j++){
			if(v[j] < v[j+1]){
				int temp = v[j];
				v[j] = v[j+1];
				v[j+1] = temp;
				sorted =false;
			}
		}
	}
}

void fn(){
	int N, X;

	cin >> N >> X; 

	vector <int> bins, files;

	for(int i = 0; i < N; i++){
		int temp; 
		cin >> temp; 
		files.push_back(temp);
	}

	sort(files.rbegin(), files.rend());

	int filledBins = 0; 

	while(!files.empty()){
		int i = bins.size() - 1;
		bool packed = false;

		while(i >= 0 && (i<=bins.size() - 1) && !packed){
			if(bins[i] + files[0] <= X){
				bins[i] += files[0];
				packed = true;
				filledBins++;

				vector<int>::iterator iter = bins.begin();
				for(int j = 0; j < i; j++)iter++;

				bins.erase(iter);
			}

			i++;
		}

		if(!packed){
			bins.push_back(files[0]);
		}

		files.erase(files.begin());

		bubbleSort(bins);
	}

	cout << bins.size() + filledBins << endl;
}

