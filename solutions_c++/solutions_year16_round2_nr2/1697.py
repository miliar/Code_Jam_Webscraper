#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <unordered_set>
#include <stack> 
#include <algorithm>
#include <math.h>
#include <sstream>
#include <functional>
#include <bitset>
#pragma comment (linker, "/STACK:167177216")
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
#define sz(a) (int)a.size()
#define pb push_back
const int MAXN = 2 * 1000 * 1000 + 500;
const double EPS = 1e-9;

bool isMaskOf(vector<char> &val, string &pattern){
	for (int i = 0; i < val.size(); ++i){
		if (pattern[i] == '?') continue;

		if (val[i] != pattern[i]) return false;
	}

	return true;
}

void toStr(int val, int fixed, vector<char> &v){
	int idx = v.size() - 1;
	while (val > 0){
		v[idx--]=(char)(val % 10 + '0');
		val /= 10;
	}

	for (int i = 0; i <= idx; ++i)v[i] = '0';
}

int main(int argc, char* argv[]) {

#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("numbers.in", "r", stdin); freopen("numbers.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);

	int ttt;
	cin >> ttt;
	forn(tt, 0, ttt){
		string a, b;
		cin >> a >> b;

		vector<char> ansa, ansb;
		int minidif = 10000;
		int minic = 10000;

		if (a.size() == 1){
			vector<char> is = vector<char>(1);
			vector<char> js = vector<char>(1);
			for (int i = 0; i <= 9; ++i){
				for (int j = 0; j <= 9; j++){
					toStr(i, 1, is);
					toStr(j, 1, js);
					if (isMaskOf(is, a) && isMaskOf(js, b)){
						if (abs(i - j) < minidif){
							minidif = abs(i - j);
							minic = i;
							ansa = is;
							ansb = js;
						}
						else{
							if (i < minic){
								minic = i;
								ansa = is;
								ansb = js;
							}
						}
					}
				}
			}
		}
		if (a.size() == 2){
			vector<char> is = vector<char>(2);
			vector<char> js = vector<char>(2);
			for (int i = 0; i <= 99; ++i){
				for (int j = 0; j <= 99; j++){
					toStr(i, 2, is);
					toStr(j, 2, js);
					if (isMaskOf(is, a) && isMaskOf(js, b)){
						if (abs(i - j) < minidif){
							minidif = abs(i - j);
							minic = i;
							ansa = is;
							ansb = js;
						}
						else{
							if (i < minic){
								minic = i;
								ansa = is;
								ansb = js;
							}
						}
					}
				}
			}
		}
		if (a.size() == 3){
			vector<char> is = vector<char>(3);
			vector<char> js = vector<char>(3);
			for (int i = 0; i <= 999; ++i){
				for (int j = 0; j <= 999; j++){
					toStr(i, 3, is);
					toStr(j, 3, js);
					if (isMaskOf(is, a) && isMaskOf(js, b)){
						if (abs(i - j) < minidif){
							minidif = abs(i - j);
							minic = i;
							ansa = is;
							ansb = js;
						}
						else{
							if (i < minic){
								minic = i;
								ansa = is;
								ansb = js;
							}
						}
					}
				}
			}
		}


		cout << "Case #" << tt + 1 << ": ";// << ansa << " " << ansb << endl;;
		for (int i = 0; i < ansa.size(); ++i)cout << ansa[i];
		cout << " ";
		for (int i = 0; i < ansa.size(); ++i)cout << ansb[i];
		cout << endl;
		//printf("\n");
	}

	return 0;
}