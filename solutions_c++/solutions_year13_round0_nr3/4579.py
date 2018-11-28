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
#include <cmath>

using namespace std;
int N, M;
void print(vector<string> &a){
	for(int i=0;i<int(a.size());i++) cout << a[i] << endl;
	cout << endl;
}
bool ispal(int c){
	vector<int> arr;
	while (c > 0){
		int t = c % 10;
		arr.push_back(t);
		c /= 10;
	}
	int st=0, end=arr.size()-1;
	while(st < end){
		if(arr[st] != arr[end]) return false;
		st++;
		end--;
	}
	return true;
}
bool isfair(int c){
	if(!ispal(c)) return false;
	int sq = int(sqrt(c));
	if(sq * sq != c) return false;
	if(!ispal(sq)) return false;
	return true;
}
int process(){
	int A, B;
	cin >> A >> B;
	int cnt = 0;
	for(int i=A;i<=B;i++){
		if(isfair(i)) cnt++;
	}
	return cnt;
}
int main(){
	string input;
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		int res  = process();
		cout << "Case #" << t+1 << ": " << res << endl;
	}
	return 0;
}

