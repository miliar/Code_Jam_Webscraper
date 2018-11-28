#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <iomanip>
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
//#define out cout
//#define in cin
using namespace std;

string toStr(int i){
	stringstream ss;
	ss << i;
	string s;
	ss >> s;
	return s;
}
int main(){
	ifstream in("A-small-attempt0.in");
	ofstream out("out.txt");
	int T;
	in >> T;
	for(int i = 0 ; i < T ; i++){
		string ans;
		int ans_;
		int r1 , r2;
		map<int,int> m;
		in >> r1;
		for(int j = 0 ; j < 4 ; j++){
			int a , b , c , d;
			in >> a >> b >> c >> d;
			if(j == r1-1)
				m[a]++,m[b]++,m[c]++,m[d]++;
		}
		in >> r2;
		for(int j = 0 ; j < 4 ; j++){
			int a , b , c , d;
			in >> a >> b >> c >> d;
			if(j == r2-1)
				m[a]++,m[b]++,m[c]++,m[d]++;
		}
		int bad = 0 , cheat = 0 ;
		for(map<int,int>::iterator it=m.begin();it!=m.end();it++){
			if(it->second == 2){
				bad++;
				ans_ = it->first;
			}else{
				cheat++;
			}
		}
		if(cheat == 8)ans = "Volunteer cheated!";
		else if(bad > 1)ans = "Bad magician!";
		else ans = toStr(ans_);
		out << "Case #" << i+1 << ": " << ans << endl;
	}
}
