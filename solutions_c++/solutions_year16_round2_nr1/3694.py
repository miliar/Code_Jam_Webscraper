#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l;
map<char,int> charCount;
map<char,int> charU;
char ks[] = {'Z','E','R','O','N','T','W','H','F','U','I','X','S','V','G'};


string tryAll(map<char,int> current, string result, int lastNum, map<char,int> currentUsage, bool& done){
	string newString = result;
	bool d = true;
	for(int k=0; k< 15; k++){
		if (currentUsage[ks[k]]!=current[ks[k]]){
			d = false;
			break;
		}
	}
	if (d){
		done = true;
		return newString;
	}
	map<char, int> newO0;
	map<char, int> newO1;
	map<char, int> newO2;
	map<char, int> newO3;
	map<char, int> newO4;
	map<char, int> newO5;
	map<char, int> newO6;
	map<char, int> newO7;
	map<char, int> newO8;
	map<char, int> newO9;
	string tmp;
	for (int i = lastNum; i < 10; i++){
		
		switch (i){
			case 0:
				tmp = newString;
				if (current['Z']>0){
					//must have zero
					currentUsage['E'] += current['Z'];
					currentUsage['R'] += current['Z'];
					currentUsage['O'] += current['Z'];
					for (int i = 0; i < current['Z'];i++){
						tmp = tmp + '0';
					}
					currentUsage['Z'] = current['Z'];
				}
				newO0 = currentUsage;
				tmp = tryAll(current, tmp, 1, newO0, done);
				break;

			case 1:
				if (currentUsage['O']+1 <= current['O'] &&
					currentUsage['N']+1 <= current['N'] &&
					currentUsage['E']+1 <= current['E']){
					//possible to be 1
					newO1 = currentUsage;
					newO1['O']++;
					newO1['N']++;
					newO1['E']++;
					tmp = tryAll(current, newString+'1', 1, newO1, done);
				}
				break;
			case 2:
				 tmp = newString;
				if (current['W']>0){
					//must have zero
					currentUsage['T'] += current['W'];
					currentUsage['O'] += current['W'];
					for (int i = 0; i < current['W'];i++){
						tmp = tmp + '2';
					}
					currentUsage['W'] = current['W'];
					
				}
				newO2 = currentUsage;
				tmp = tryAll(current, tmp, 3, newO2, done);
				break;
			case 3:
				if (currentUsage['T']+1 <= current['T'] &&
					currentUsage['H']+1 <= current['H'] &&
					currentUsage['R']+1 <= current['R'] &&
					currentUsage['E']+2 <= current['E']){
					//possible to be 1
					newO3 = currentUsage;
					newO3['T']++;
					newO3['H']++;
					newO3['R']++;
					newO3['E']++;newO3['E']++;
					tmp = tryAll(current, newString+'3', 3, newO3, done);
				}
				break;
			case 4:
				 tmp = newString;
				if (current['U']>0){
					//must have zero
					currentUsage['F'] += current['U'];
					currentUsage['O'] += current['U'];
					currentUsage['R'] += current['U'];
					for (int i = 0; i < current['U'];i++){
						tmp = tmp + '4';
					}
					currentUsage['U'] = current['U'];
				}
				newO4 = currentUsage;
				tmp = tryAll(current, tmp, 5, newO4, done);
				break;
			case 5:
				if (currentUsage['F']+1 <= current['F'] &&
					currentUsage['I']+1 <= current['I'] &&
					currentUsage['V']+1 <= current['V'] &&
					currentUsage['E']+1 <= current['E']){
					//possible to be 1
					newO5 = currentUsage;
					newO5['F']++;
					newO5['I']++;
					newO5['V']++;
					newO5['E']++;
					tmp = tryAll(current, newString+'5', 5, newO5, done);
				}
			break;
			case 6:
				 tmp = newString;
				if (current['X']>0){
					//must have zero
					currentUsage['S'] += current['X'];
					currentUsage['I'] += current['X'];
					for (int i = 0; i < current['X'];i++){
						tmp = tmp + '6';
					}
					currentUsage['X'] = current['X'];
				}
				newO6 = currentUsage;
				tmp = tryAll(current, tmp, 7, newO6, done);
				break;
			case 7:
				if (currentUsage['S']+1 <= current['S'] &&
					currentUsage['E']+2 <= current['E'] &&
					currentUsage['V']+1 <= current['V'] &&
					currentUsage['N']+1 <= current['N']){
					//possible to be 1
					newO7 = currentUsage;
					newO7['S']++;
					newO7['E']++;newO7['E']++;
					newO7['V']++;
					newO7['N']++;
					tmp = tryAll(current, newString+'7', 7, newO7, done);
				}
				break;
			case 8:
				 tmp = newString;
				if (current['G']>0){
					//must have zero
					currentUsage['E'] += current['G'];
					currentUsage['I'] += current['G'];
					currentUsage['H'] += current['G'];
					currentUsage['T'] += current['G'];
					for (int i = 0; i < current['G'];i++){
						tmp = tmp + '8';
					}
					currentUsage['G'] = current['G'];
				}
				newO8 = currentUsage;
				tmp = tryAll(current, tmp, 9, newO8, done);
				break;
			case 9:
				if (currentUsage['N']+2 <= current['N'] &&
					currentUsage['I']+1 <= current['I'] &&
					currentUsage['E']+1 <= current['E']){
					//possible to be 1
					newO9=currentUsage;
					newO9['N']++;newO9['N']++;
					newO9['E']++;
					newO9['I']++;
					tmp = tryAll(current, newString+'9', 9, newO9, done);
				}
		}
		if (done){
			return tmp;
		}
	}
	return newString;
}

int main() {
    //freopen("x.in", "r", stdin);

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	char ks[] = {'Z','E','R','O','N','T','W','H','F','U','I','X','S','V','G'};
	F1(tt,tn) {
		//cerr << tt << endl;
		for(int k=0; k< 15; k++){
			charCount[ks[k]] = 0;
			charU[ks[k]] = 0;
		}
		bool d = false;
		string s; cin >> s;
		string q;
		for (int j = 0; j < s.length(); j++){
			char c = s.at(j);
			charCount[c]++;
		}
		map<char, int> newS (charCount);
		q = tryAll(charCount, q, 0, charU, d);
		
  		printf("Case #%d: ", tt);
		cout << q << endl;
	}
	return 0;
}
