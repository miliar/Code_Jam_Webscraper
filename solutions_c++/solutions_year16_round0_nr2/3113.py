#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

inline bool allTrue(const vector<bool>& a){
	for(int i=0; i<a.size(); i++) if(!a[i]) return false;
	return true;
}

inline int numLeft(const vector<bool>& a){
	for(int i=a.size()-1; i>=0; i--){
		if(!a[i]) return i+1;
	}
	return 0;
}

inline int leftPluses(const vector<bool>& a){
	int i=0;
	while(i<a.size() && a[i]) i++;
	return i;
}

void flip(vector<bool>& a, int num, int& totalFlips){
	for(int i=0; i<num; i++) a[i] = !a[i];
	reverse(a.begin(), a.begin()+num);
	totalFlips++;
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		string s;
		cin>>s;
		int totalFlips = 0;
		int n = s.size();
		vector<bool> a(n);
		for(int i=0; i<n; i++) a[i] = (s[i]=='-')?false:true;
		int left;
		while((left=numLeft(a))>0){
			if(a[0]){
				int toFlip = leftPluses(a);
				flip(a, toFlip, totalFlips);
			}
			flip(a, left, totalFlips);
		}
		cout<<"Case #"<<testnum+1<<": "<<totalFlips<<endl;
	}
	return 0;
}
