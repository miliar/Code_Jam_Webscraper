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

using namespace std;
int main(){
	int t;
	string str;
	int len,i,count;
	cin >> t;
	for(int ti=1;ti<=t;++ti){
		cin >> str;
		vector<int> a(256,0);
		len = str.length();
		for(i=0;i<len;++i){
			a[str[i]]++;
		}
		vector<int> ans;
		if(a['Z']!=0){
			count = a['Z'];
			for(i=0;i<count;++i) ans.push_back(0);
			a['E']-=a['Z'];
			a['R'] -= a['Z'];
			a['O'] -= a['Z'];
			a['Z'] = 0;
		}
		if(a['W']!=0){
			count = a['W'];
			for(i=0;i<count;++i) ans.push_back(2);
			a['T']-=a['W'];
			a['O'] -=a['W'];
			a['W'] = 0;
		}
		if(a['G']!=0){
			count = a['G'];
			for(i=0;i<count;++i) ans.push_back(8);
			a['E'] -= a['G'];
			a['I'] -= a['G'];
			a['H'] -= a['G'];
			a['T'] -= a['G'];
		}
		if(a['X']!=0){
			count = a['X'];
			for(i=0;i<count;++i) ans.push_back(6);
			a['S'] -= count;
			a['I'] -= count;
			a['X'] =0;
		}
		if(a['U']!=0){
			count = a['U'];
			for(i=0;i<count;++i) ans.push_back(4);
			a['F'] -= count;
			a['O'] -= count;
			a['R'] -= count;
			a['U'] = 0;
		}
		if(a['S']!=0){
			count = a['S'];
			for(i=0;i<count;++i) ans.push_back(7);
			a['E'] -= count;
			a['V'] -= count;
			a['E'] -= count;
			a['N'] -= count;
			a['S'] = 0;
		}
		if(a['R']!=0){
			count = a['R'];
			for(i=0;i<count;++i) ans.push_back(3);
			a['T'] -= count;
			a['H'] -= count;
			a['E'] -= count;
			a['E'] -= count;
			a['R'] = 0;
		}
		if(a['F']!=0){
			count = a['F'];
			for(i=0;i<count;++i) ans.push_back(5);
			a['I'] -= count;
			a['V'] -= count;
			a['E'] -= count;
			a['F'] = 0;
		}
		if(a['V']!=0){
			count = a['V'];
			for(i=0;i<count;++i) ans.push_back(7);
			a['S'] -= count;
			a['E'] -= count;
			a['E'] -= count;
			a['N'] -= count;
			a['V'] = 0;
		}
		if(a['O']!=0){
			count = a['O'];
			for(i=0;i<count;++i) ans.push_back(1);
			a['N'] -= count;
			a['E'] -= count;
			a['O'] = 0;
		}
		if(a['I']!=0){
			count = a['I'];
			for(i=0;i<count;++i) ans.push_back(9);
		}
		sort(ans.begin(),ans.end());
		cout << "Case #" <<ti << ": ";
		for(int i=0;i<ans.size();++i) cout << ans[i];
			cout << endl;
	}
}