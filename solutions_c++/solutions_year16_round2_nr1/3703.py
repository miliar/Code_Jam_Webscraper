/*
 * ANew.cpp
 * 
 * Created by: Ashik <ashik@KAI10>
 * Created on: 2016-04-30 
 */


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define mem(list, val) memset(list, (val), sizeof(list))
#define pb push_back

bool present(string a, string b){
	bool taken[a.size()];
	for(int i=0; i<a.size(); i++) taken[i] = false;
	
	for(int i=0; i<b.size(); i++){
		bool ret = false;
		for(int j=0; j<a.size(); j++){
			if(a[j] == b[i] && !taken[j]){
				ret = true;
				taken[j] = true;
				break;
			}
		}
		if(!ret) return false;
	}
	return true;
}

string nw(string a, string b){
	string ret="";
	bool take[a.size()];
	for(int i=0; i<a.size(); i++) take[i] = true;
	
	for(int i=0; i<b.size(); i++){
		for(int j=0; j<a.size(); j++){
			if(a[j] == b[i] && take[j]){
				//cout << j << ' ' << a[j] << endl;
				take[j] = false;
				break;
			}
		}
	}
	
	for(int i=0; i<a.size(); i++) if(take[i] == true) {ret.pb(a[i]);} //cout << a[i] << endl;};
	
	return ret;
}

string all[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

vector<int> ans;

bool recur(string in, int ind)
{
	if(in.size() == 0) return true;
	if(ind == 10) return false;
	
	bool ret;
	
	if(present(in, all[ind])){
		ans.pb(ind);
		//cout << ind << endl;
		ret = recur(nw(in, all[ind]), ind);
		
		if(!ret){
			ans.pop_back();
			return recur(in, ind+1);
		}
		
		else return ret;
	}
	
	else return recur(in, ind+1);
}

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output", "w", stdout);
	
	int t, cs = 0;
	scanf("%d", &t);
	while(t--){
		string in;
		cin >> in;
		
		recur(in, 0);
		
		printf("Case #%d: ", ++cs);
		for(int i=0; i<ans.size(); i++) printf("%d", ans[i]);
		puts("");
		ans.clear();
	}
	return 0;
}
