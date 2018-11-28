#include <iostream>
#include <cstdio>
#include <unordered_map>
#include <vector>
#include <cstring>
using namespace std;

bool canFind(const string& s, unordered_map<char,int> myMap){
	for(int i =0 ; i < s.size(); ++i){
		if(myMap.find(s[i]) == myMap.end() || myMap.find(s[i]) != myMap.end() && myMap.find(s[i])->second == 0)
			return false;
		myMap[s[i]]--;
	}
	return true;
}

void subtract(const string& s, unordered_map<char,int>& myMap){
	for(int i =0 ; i < s.size(); ++i){
		if(myMap.find(s[i]) != myMap.end() && myMap.find(s[i])->second > 0){
			myMap[s[i]]--;
		}
	}
}

void readd(const string& s, unordered_map<char,int>& myMap){
	for(int i =0 ; i < s.size(); ++i){
		myMap[s[i]]++;
	}
}
bool isEmpty(const unordered_map<char,int>& myMap){
	for(auto s = myMap.begin(); s!=myMap.end(); ++s){
		if(s->second != 0)
			return false;
	}
	return true;
}
string gSol = "";
void buildSolution(const vector<string>& v, unordered_map<char,int>& myMap, string sol, int k){
	if(isEmpty(myMap)){
		gSol = sol;
		return;
	}
	for(int i =0 ; i < v.size(); ++i){
		if(canFind(v[i], myMap)){
			sol += i+'0';
			subtract(v[i], myMap);
			buildSolution(v, myMap, sol, k+1);
			if(gSol != "")
				return;
			sol.pop_back();
			readd(v[i], myMap);
		}
	}
}
string solve(const char s[]){
	string sol = "";
	unordered_map<char, int> myMap;
	int len = strlen(s);
	for(int i = 0; i < len; ++i){
		if(myMap.find(s[i]) != myMap.end()){
			myMap[s[i]]++;
		}else{
			myMap.insert(pair<char,int>(s[i],1));
		}
	}
	vector<string> v = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE",
	"SIX", "SEVEN", "EIGHT", "NINE"};
	int start = 0;
	buildSolution(v, myMap, sol, 0);
	return gSol;
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i = 0; i < t; ++i){
		gSol = "";
		char s[2005];
		scanf("%s", s);
		cout << "Case #" << (i+1) << ": " << solve(s) << endl;
	}
	return 0;
}

