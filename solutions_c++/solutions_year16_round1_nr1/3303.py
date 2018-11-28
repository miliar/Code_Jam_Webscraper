/*
ID: vovanhu1
PROG: hamming
LANG: C++11
*/

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <set>
#include <list>
#include <vector>
//#include <unordered_map>



using namespace std;

typedef pair<int, int> PII;
typedef pair<long long, long long> PLL;


template<typename T>
void display(T a[], int size){
	for(int i = 0; i < size-1; i++){
		cout<<a[i]<<" ";
	}
	cout<<a[size-1]<<endl;
}

// template<typename T>
// void display(T** a, int row, int col){
// 	for(int i = 0; i < row; i++){
// 		for(int j = 0; j < col-1; j++){
// 			cout<<a[i*col +j<<" ";	
// 		}
// 		cout<<a[i][col-1]<<endl;
// 	}
// 	cout<<endl;
// }


void display(vector<PII> a){
	for(int i = 0; i < a.size(); i++){
		cout<<"("<<a[i].first<<","<<a[i].second<<")"<<" ";
	}
	cout<<endl;
}

template<typename T>
void initialise(T a[], T value, int length){
	for(int i = 0; i < length; i++) a[i] = value;
}



template<typename T>
T max(T a[], T initMax, int length){
	T max = initMax;
	for(int i = 0; i < length; i++){
		if(a[i] > max) max = a[i];
	}
	return max;
}

// template<typename T>
// bool find(T a[], T s, int n){
// 	int left = 0;
// 	int right = n -1;
// 	while(left < right){
// 		int mid = (left+right)/2;
// 		if(s.compare(a[mid]) == 0) return true;
// 		else if(s.compare(a[mid]) < 0){
// 			right = mid;
// 		}
// 		else{
// 			left = mid + 1;
// 		}
// 	}
// 	return false;
// }

void factor(int a[], int base, int num, int n){
	for(int i = n - 1; i >= 0; i--){
		a[i] = num % base;
		num = num/base;
	}
}


int findLength(int n, int base){
	int i = 0;
	while(n > 0){
		i++;
		n = n/base;
	}
	return i;
}

bool compare1(PII a, PII b){
	if(a.second != b.second) return a.second < b.second;
	else return a.first < b.first;
}

bool compare2(PII a, PII b){
	if(a.first != b.first) return a.first < b.first;
	else return a.second < b.second;

}

int find(vector<PII> a, int target, int begin, int end){
	if(a[end].first < target) return -1;
	int left = begin;
	int right = end;
	while(left < right){
		int mid = (left+right)/2;
		if(a[mid].first >= target){
			right = mid;
		}
		else{
			left = mid + 1;
		}
	}
	
	return left;
}



int main(){
	ofstream fout("A-small.out");

	
	int t; cin>>t;
	for(int test = 0; test < t; test++){
		string word;
		cin>>word;
		list<char> res;
		res.push_back(word[0]);
		// res[0] = 'H';
		// cout<<res<<endl;
		for(int i = 1; i < word.length(); i++){
			if((int)word[i] >= (int)(*res.begin())) res.push_front(word[i]);
			else res.push_back(word[i]);
		}
		string final = word;
		for(int i = 0; i < final.length(); i++){
			final[i] =	*res.begin(); 
			// if(temp) final[i] = temp;
			res.pop_front(); 
		}

		fout<<"Case #"<<test+1<<": "<<final<<endl;

	}	
}


