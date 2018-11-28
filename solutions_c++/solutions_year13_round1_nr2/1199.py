#include <stdexcept>
#include <cassert>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <stack>
#include <list>
#include <map>
#include <queue>
#include <cmath>
#include <climits>
#include <ctime>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <utility>
#include <set>
using namespace std;

#ifndef COMMON_H
#define COMMON_H

template <class E>
void print_vector(vector<E> A){
    for(int i = 0; i < (int)A.size(); i++){
        cout << A[i] << "\t";
    }
    cout << endl;
}

template <class E>
void print_matrix(vector<vector<E> > A){
    for(int i = 0; i <(int)A.size(); i ++){
        vector<E> tv = A[i];
        for(int j = 0; j < (int)tv.size(); j++){
            cout << tv[j] << "\t";
        }
        cout << endl;
    }
    cout << endl;
}

void print_array(int* A, int sz){
    for(int i = 0; i < sz; i++){
        cout << A[i] << "\t";
    }
    cout << endl;
}

template <class T>
void print_array(T* A, int sz){
    for(int i = 0; i < sz; i++){
        cout << A[i] << "\t";
    }
    cout << endl;
}

template <class T>
void print_vector(vector<T> A, int beg, int end){
    for(int i = beg; i < end; i ++)
        cout << A[i] << "\t";    
    cout << endl;
}

void print_vector(vector<pair<int, int> > A){
    for(int i = 0; i < (int)A.size(); i++){
        cout << "(" << A[i].first << ", " << A[i].second << ") ";
    }
    cout << endl;
}

void swap(vector<int>& A, int a, int b){
    int t = A[a];
    A[a] = A[b];
    A[b] = t;
}

void swap(int& a, int& b){
    int t = a;
    a = b;
    b = t;
}

void swap(int*& A, int a, int b){
    int t = A[a];
    A[a] = A[b];
    A[b] = t;
}

void swap(string& A, int a, int b){
    char t = A[a];
    A[a] = A[b];
    A[b] = t;
}

template <class T>
bool check_vector(vector<T> A,vector<T> B){
    if(A.size() != B.size())
        return false;
    for(int i = 0; i < (int)A.size(); i++){
        if(A[i] != B[i])
            return false;
    }
    return true;
}

template <class T, class E>
bool check_vector(vector<pair<T,E> > A, vector<pair<T,E> > B){
    if(A.size() != B.size())
        return false;
    for(int i = 0; i < (int)A.size(); i++){
        if(A[i].first == B[i].first && A[i].second == B[i].second){
            //do nothing
        }else{
            return false;
        }
    }
    return true;
}

template <class T> 
bool check_matrix(vector<vector<T> > A, vector<vector<T> > B){
    if(A.size() != B.size())
        return false;    
    int sz = (int)A.size();
    for(int i = 0; i < sz; i++){
        if(A[i].size() != B[i].size())
            return false;
        for(int j = 0; j < (int)A[i].size(); j++){
            if(A[i][j] != B[i][j])
                return false;
        }
    }
    return true;
}

void message(bool flag, string msg = ""){
    if(flag){
        cout << "\tpass\t" << msg << endl;
    }else{
        cout << "\tfail\t" << msg << endl;
    }
}
#endif

 


long long energy, regain, num;
vector<long long> val;

void solve(long long step, long long all, long long path, long long &ret) {
	if (num == step) {
		ret = max(ret, path);
		return;	
	}	
	for (long long j = 0; j <= all; j++) {
		solve(step+1, min(energy,all-j+regain), path+j*val[step], ret);	
	}
}



void read_line(string inFileName, string outFileName){
	ifstream inFile(inFileName.c_str());
	ofstream outFile(outFileName.c_str());
	int T = 0;
	inFile >> T;
	for (int t = 1; t <= T; t++) {
		inFile >> energy;
		inFile >> regain;
		inFile >> num;
		val.resize(num);
		for (int i = 0; i < num; i++) {
			inFile >> val[i];	
		}		
		long long ret = 0;
		long long path = 0;
		solve(0, energy, path, ret);		
		outFile << "Case #" << t << ": " << ret << endl;
	}
	inFile.close();
	outFile.close();
}


int main() {
	string inFileName = "./data2.dat";
	string outFileName = "./result2.dat";
	read_line(inFileName, outFileName);
	return 0;	
}
