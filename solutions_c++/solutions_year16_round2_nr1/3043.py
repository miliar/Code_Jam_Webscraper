#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int T = 1; T<=t; T++){
		string s;
		cin>>s;
		string ans;
		map<char,int> mp;
		for(char c: s)	mp[c]++;
		vector<string> arr ={"ZERO", "FOUR", "SIX", "FIVE", "SEVEN", "EIGHT", "THREE", "NINE", "ONE", "TWO"};
		map<int,int> mm;
		mm[0]=0;
		mm[1]=4;
		mm[2]=6;
		mm[3]=5;
		mm[4]=7;
		mm[5]=8;
		mm[6]=3;
		mm[7]=9;
		mm[8]=1;
		mm[9]=2;
		for(int i = 0 ; i<arr.size(); i++){
			map<char,int> req;
			for(char c : arr[i]){
				req[c]++;
			}
			int pos = 1;
			// cout<<"For i = "<<i<<endl;
			// for(auto j : mp)	cout<<j.first<<" "<<j.second<<endl;
			//for()
			for(auto j : req){
				if(mp[j.first]<j.second)	pos=0;
			}
			if(pos){
				//cout<<mm[i]<<"t\n";
				ans+=to_string(mm[i]);
				for(auto j : req){
					mp[j.first]-=j.second;
				}
				i--;
				continue;
			}
		}
		//for(auto j : mp)	if(j.second!=0)	cout<<"here";
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<T<<": "<<ans<<"\n";
	}
	
	return 0;
}