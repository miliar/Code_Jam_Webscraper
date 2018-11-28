#include <iostream>
#include <vector>
#include <sstream>
#include <cstdio>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

int conts[30];
string numbers[10] = {"ZERO","TWO","SIX","FOUR","FIVE","SEVEN","EIGHT","ONE","NINE","THREE"};
string equil[10] = {"0","2","6","4","5","7","8","1","9","3"};

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin>>T;
	string s;
	for(int k = 1; k <= T; k++) {
		cin>>s;
		string res = "";
		for(int i = 0; i < 30; i++)
				conts[i] = 0;
		for(int i = 0; i < s.size(); i++) {
			conts[s[i] - 'A']++;
		}
		int x = 0;
		while(x < 10) {
			string num = numbers[x];
			bool canGenerate = true;
			for(int i = 0; i < num.size(); i++) {
				if(conts[num[i] - 'A'] == 0)
					canGenerate = false;
				conts[num[i] - 'A']--;
			}

			if(canGenerate) {
				res += equil[x];
			}
			else {
				x++;
				for(int i = 0; i < num.size(); i++) {
					conts[num[i] - 'A']++;
				}
			}
			sort(res.begin(),res.end());

		}
		cout<<"Case #"<<k<<": "<<res<<endl;
	}

	return 0;
}