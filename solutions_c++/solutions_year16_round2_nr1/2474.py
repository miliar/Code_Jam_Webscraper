#include <iostream>
#include <unordered_map>
#include <string>
#include <set>
#include <vector>
#include <algorithm>    // std::sort

using namespace std;

int main(){
	int T;
	cin>>T;
	string s;
	int x=0;
	vector<string> v;
	v.push_back("ONE");
	v.push_back("THREE");
	v.push_back("FIVE");
	v.push_back("SEVEN");
	v.push_back("NINE");
	unordered_map<string, int> dict;
	dict["ONE"]=1;
	dict["THREE"]=3;
	dict["FIVE"]=5;
	dict["SEVEN"]=7;
	dict["NINE"]=9;

	while(T--){
		cin>>s;
		x++;
		string re = "";
		unordered_map<char, int> mp;
		for(auto c:s){
			mp[c]++;
		}
		vector<int> result;
		while(mp['Z']>0){
			result.push_back(0);
			mp['Z']--;
			mp['E']--;
			mp['R']--;
			mp['O']--;
		}
		while(mp['W']>0){
			result.push_back(2);
			mp['T']--;
			mp['W']--;
			mp['O']--;
		}
		while(mp['U']>0){
			result.push_back(4);
			mp['F']--;
			mp['O']--;
			mp['U']--;
			mp['R']--;
		}
		while(mp['X']>0){
			result.push_back(6);
			mp['S']--;
			mp['I']--;
			mp['X']--;
		}
		while(mp['G']>0){
			result.push_back(8);
			mp['E']--;
			mp['I']--;
			mp['G']--;
			mp['H']--;
			mp['T']--;
		}
		for(auto num:v){
			bool flag=true;
			while(flag){
				unordered_map<char, int> mpcopy = mp;
				for(auto c:num){
					if(mpcopy[c]>0){
						mpcopy[c]--;
					}else{
						flag=false;
						break;
					}
				}
				if(flag){
					mp = mpcopy;
					result.push_back(dict[num]);
				}
			}
		}
		sort(result.begin(),result.end());
		cout << "Case #"<<x<<": ";
		for(auto x:result){
			cout<<x;
		}
		cout<<endl;
	}
	return 0;
}
