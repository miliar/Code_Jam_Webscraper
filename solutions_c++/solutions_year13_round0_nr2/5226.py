/*
 * =====================================================================================
 *
 *       Filename:  tic-tac.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 13 April 2013 10:08:01  IST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:   (), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int N, M;
void print(vector<string> &a){
	for(int i=0;i<int(a.size());i++) cout << a[i] << endl;
	cout << endl;
}
bool validrow(int r, int c, int lawn[100][100]){
	int cur = lawn[r][c];
	for(int i=0;i<M;i++) if(lawn[r][i] > cur) return false;
	return true;
}
bool validcol(int r, int c, int lawn[100][100]){
	int cur = lawn[r][c];
	for(int i=0;i<N;i++) if(lawn[i][c] > cur) return false;
	return true;
}

string process(){
	cin >> N >> M;
	int lawn[100][100];
	for(int i=0;i<N;i++) for(int j=0;j<M;j++){
		int v;
		cin >> v;
		lawn[i][j] = v;
	}
	for(int i=0;i<N;i++) for(int j=0;j<M;j++){
		if(validrow(i, j, lawn) == false and validcol(i,j, lawn) == false) return "NO";
	}
	return "YES";
}
int main(){
	string input;
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		string res = process();
		cout << "Case #" << t+1 << ": " << res << endl;
	}
	return 0;
}

