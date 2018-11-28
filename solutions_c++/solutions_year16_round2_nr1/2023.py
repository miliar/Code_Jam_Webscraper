#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <vector>
#include <set>
#include <queue>
#include <bitset>
#include <map>

using namespace std;

string arr[] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;

	for(int t=1; t<=test; t++) {
		cout<<"Case #"<<t<<": ";
		string s;
		cin>>s;

		int cnt[26] = {0};

		for(int i=0; i<s.size(); i++)
			cnt[s[i]-'A']++;

		vector<int> dig;

		//Zero
		for(int i=0; i<cnt[25]; i++) {
			dig.push_back(0);
			cnt['E'-'A']--;
			cnt['R'-'A']--;
			cnt['O'-'A']--;			
		}

		//Two
		for(int i=0; i<cnt['W'-'A']; i++) {
			dig.push_back(2);
			cnt['T'-'A']--;
			cnt['O'-'A']--;
		}

		//Four
		for(int i=0; i<cnt['U'-'A']; i++) {
			dig.push_back(4);
			cnt['F'-'A']--;
			cnt['O'-'A']--;
			cnt['R'-'A']--;
		}

		//Six
		for(int i=0; i<cnt['X'-'A']; i++) {
			dig.push_back(6);
			cnt['S'-'A']--;
			cnt['I'-'A']--;
		}

		//Eight
		for(int i=0; i<cnt['G'-'A']; i++) {
			dig.push_back(8);
			cnt['E'-'A']--;
			cnt['I'-'A']--;
			cnt['H'-'A']--;
			cnt['T'-'A']--;
		}

		//five
		for(int i=0; i<cnt['F'-'A']; i++) {
			dig.push_back(5);
			cnt['I'-'A']--;
			cnt['V'-'A']--;
			cnt['E'-'A']--;
		}

		//Seven
		for(int i=0; i<cnt['V'-'A']; i++) {
			dig.push_back(7);
			cnt['S'-'A']--;
			cnt['E'-'A']--;
			cnt['E'-'A']--;
			cnt['N'-'A']--;
		}

		//Nine
		for(int i=0; i<cnt['I'-'A']; i++) {
			dig.push_back(9);
			cnt['N']-=2;
			cnt['E']--;
		}

		//One
		for(int i=0; i<cnt['O'-'A']; i++) {
			dig.push_back(1);
		}

		//Three

		for(int i=0; i<cnt['R'-'A']; i++) {
			dig.push_back(3);
		}

		sort(dig.begin(), dig.end());

		for(int i=0; i<dig.size(); i++) {
			cout<<dig[i];
		}

		cout<<endl;
	}

}