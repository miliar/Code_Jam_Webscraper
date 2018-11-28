#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;

void gen(){
	freopen("testcase.txt", "w", stdout);
	exit(0);
}

char get(char a, char b){
	if(a > b)
		swap(a, b);
	if(a == 'P' && b == 'R')
		return 'P';
	if(a == 'P' && b == 'S')
		return 'S';
	if(a == 'R' && b == 'S')
		return 'R';
}

bool check(string cur){
	if(cur.size() == 1){
		return true;
	}
	string next;
	for(int i=0; i<cur.size(); i+=2){
		if(cur[i] == cur[i+1]){
			return false;
		}
		next += get(cur[i], cur[i+1]);
	}
	return check(next);
}

string slow(int n, int r, int p, int s){
	vector<char> arr;
	for(int i=0; i<r; i++){
		arr.push_back('R');
	}
	for(int i=0; i<p; i++){
		arr.push_back('P');
	}
	for(int i=0; i<s; i++){
		arr.push_back('S');
	}

	vector<int> pr(arr.size());
	for(int i=0; i<pr.size(); i++){
		pr[i] = i;
	}

	string res;

	do{
		string cur;
		for(int i=0; i<pr.size(); i++){
			int ind = pr[i];
			cur += arr[ind];
		}

		if(check(cur)){
			if(res.size() == 0){
				res = cur;
			}
			else{
				if(cur < res){
					res = cur;
				}
			}
		}
	}
	while(next_permutation(pr.begin(), pr.end()));


	if(res.size() == 0){
		res = "IMPOSSIBLE";
	}
	return res;
}

char buf[3] = {'P', 'R', 'S'};

string get_res(int n, string str){
	for(int i=1; i<n; i++){
		string next;

		int len = 1 << i;

		for(int j=0; j<str.size(); j += 2*len){
			string a, b;
			a = str.substr(j, len);
			b = str.substr(j+len, len);
			if(a > b){
				swap(a, b);
			}
			next += a;
			next += b;
		}

		str = next;
	}

	return str;
}

string fast(int n, int r, int p, int s){
	string res;
	for(int i=0; i<3; i++){
		string cur;
		cur += buf[i];

		for(int j=0; j<n; j++){
			string next;
			for(int k=0; k<cur.size(); k++){
				if(cur[k] == 'P'){
					next += "PR";
				}
				if(cur[k] == 'R'){
					next += "RS";
				}
				if(cur[k] == 'S'){
					next += "PS";
				}
			}
			cur = next;
		}

		int rr = 0, pp = 0, ss = 0;
		for(int j=0; j<cur.size(); j++){
			if(cur[j] == 'P'){
				pp++;
			}
			if(cur[j] == 'R'){
				rr++;
			}
			if(cur[j] == 'S'){
				ss++;
			}
		}

		if(rr == r && pp == p && ss == s){
			string str = get_res(n, cur);
			if(res.size() == 0){
				res = str;
			}
			else{
				if(str < res){
					res = str;
				}
			}
		}
	}

	if(res.size() == 0){
		res = "IMPOSSIBLE";
	}
	return res;
}

int main(){

#ifdef _CONSOLE
	freopen("A-large.in", "r", stdin);
	//freopen("testcase.txt", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int countTest;
	cin>>countTest;	
	for(int test = 1; test <= countTest; test++){
		int n, r, p, s;
		cin>>n>>r>>p>>s;

		//string res2 = slow(n, r, p, s);
		string res = fast(n, r, p, s);

		//if(res != res2){
		//	cerr<<"NO "<<test<<"\n";
		//	cerr<<res2<<" "<<res<<"\n\n";
		//}

		printf("Case #%d: ", test);
		cout<<res<<"\n";
		cerr<<test<<"\n";
	}
	
	return 0;
}

