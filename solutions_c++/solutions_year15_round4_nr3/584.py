#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <stdlib.h>
#include <assert.h>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;
typedef long long lint;
int t, n, m;
vector<int> eng, fre, sen[20];

map<string, int> id;

int hash[3000];
char s[12000];
char word[100];
int cnt = 0;

int main() {
	scanf("%d\n", &t);
	for(int cas = 1; cas <= t; cas++) {
		scanf("%d\n", &n);
		m = 0;
		id.clear();

		//eng
		eng.clear();
		cin.getline(s, 11000);
		cnt = 0;
		for(int i = 0; ; i++) {
			if(s[i] == ' ' || s[i] == 0) {
				word[cnt++] = 0;
				string a(word);
				if(id.find(a) == id.end()) {
					id[a] = m++;
				}
				eng.push_back(id[a]);
				cnt = 0;
			}
			if(s[i] == 0) {
				break;
			}
			if(s[i] != ' ') word[cnt++] = s[i];
		}

		//fre
		fre.clear();
		cin.getline(s, 11000);
		cnt = 0;
		for(int i = 0; ; i++) {
			if(s[i] == ' ' || s[i] == 0) {
				word[cnt++] = 0;
				string a(word);
				if(id.find(a) == id.end()) {
					id[a] = m++;
				}
				fre.push_back(id[a]);
				cnt = 0;
			}
			if(s[i] == 0) {
				break;
			}
			if(s[i] != ' ') word[cnt++] = s[i];
		}

		sen[0].clear();
		for(int i = 0; i < n - 2; i++) {
			sen[i].clear();
			cin.getline(s, 11000);
			cnt = 0;
			for(int j = 0; ; j++) {
				if(s[j] == ' ' || s[j] == 0) {
					word[cnt++] = 0;
					string a(word);
					if(id.find(a) == id.end()) {
						id[a] = m++;
					}
					sen[i].push_back(id[a]);
					cnt = 0;
				}
				if(s[j] == 0) {
					break;
				}
				if(s[j] != ' ') word[cnt++] = s[j];
			}
		}

		int ans = 1e9;
		for(int i = 0; i < (1 << (n - 2)); i++) {
			int tmp = 0;
			memset(hash, 0, sizeof(hash));
			for(int j = 0; j < eng.size(); j++) {
				hash[eng[j]] = 1;
			}
			for(int j = 0; j < n - 2; j++) {
				if(i & (1 << j)) {
					for(int k = 0; k < sen[j].size(); k++) {
						hash[sen[j][k]] = 1;	
					}
				}
			}
			for(int j = 0; j < n - 2; j++) {
				if((i & (1 << j)) == 0) {
					for(int k = 0; k < sen[j].size(); k++) {
						if(hash[sen[j][k]] == 1) {
							hash[sen[j][k]] = 0;
							tmp++;
						}
					}
				}
			}
			for(int j = 0; j < fre.size(); j++) {
				if(hash[fre[j]] == 1) {
					tmp++;
					hash[fre[j]] = 0;
				}
			}

			ans = min(ans, tmp);
		}
		cerr << cas << endl;
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
