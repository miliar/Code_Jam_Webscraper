#include <iostream>
#include <string>
#include <queue>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <climits>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef vector<int> vi;


string s;
int k;
void flip_from(int idx){
	for(int i = idx; i < idx + k; i ++){
		s[i] = (s[i] == '-') ? '+' : '-';
	}
}
int first_blank(){
	for(int i = 0; i < s.size(); i ++){
		if(s[i] == '-')
			return i;
	}
	return -1;
}
bool has_blank(){
	for(int i = 0; i < s.size(); i ++){
		if(s[i] == '-')
			return true;
	}
	return false;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out.txt", "r+", stdout);
#endif
	int case_num = 1;
	int t; cin >> t;
	while(t--){
		cin >> s >> k;
		int ans = 0;
		bool impossible = false;
		while(has_blank() && !impossible){
			int blank = first_blank();
			if(blank >= s.size() - (k - 1) )
				impossible = true;
			else 
				flip_from(blank);
			ans ++;
		}
		cout << "Case #" << case_num ++ << ": ";
		if(impossible) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}
