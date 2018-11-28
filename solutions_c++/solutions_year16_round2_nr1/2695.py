#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <string>
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
#include <cstring>
#include <fstream>

using namespace std;

int INF = 1E9;

vector <string> dig = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int alp[26];
int ord[10] = {0,6,7,5,8,3,4,9,1,2};

bool can(int at){
	for(char ch : dig[at])
		alp[ch-'A']--;
	bool ret = true;
	for(char ch : dig[at])
		if(alp[ch-'A'] < 0)
			ret = false;
	if(!ret)
		for(char ch:dig[at])
			alp[ch-'A']++;
	return ret;
}

int main() {
	freopen("A-large.in", "r", stdin);
	ofstream fout;
	fout.open("answer.out");

	int T;
	cin>>T;
	

	for(int Case = 1; Case <= T; Case++){
		fout<<"Case #"<<Case<<": ";
		//fout<<endl;
		string str;
		cin>>str;
		memset(alp, 0, sizeof(alp));
		for(char ch:str) ++alp[ch-'A'];
		string res = "";
		int cnt[10] = {0};
		for(int i = 0; i < 10; i++){
			while(can(ord[i])){
				cnt[ord[i]]++;
			}
		}
		for(int i = 0; i < 10; i++)
			while(cnt[i] != 0){
				res += ('0' + i);
				cnt[i]--;
			}
		fout<<res<<endl;

		//fout<<endl;
	}
	return 0;
}
