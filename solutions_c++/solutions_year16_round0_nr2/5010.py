#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <iomanip>
#include <set>
#include <cstdio>
#include <cstring>
#include <stack>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <bitset>
#include <ctime>
#include <list>
#include <functional>
using namespace std;
#define mp make_pair
#define ull unsigned long long
#define ll long long
#define mod1 (ll)1000000009
#define mod (ll)1000000007
#define inf (ll)1600000016000000000
#define mpi acos(-1.0)
#define M_E (double)2.71828182846
#pragma comment(linker, "/STACK:1000000000")

static int m1[10];

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t, n;
	cin >> t;
	string s;
	for (int tt = 0; tt < t; ++tt){
		cin >> s;
		cout << "Case #" << tt + 1 << ": ";
		int a = 0;
		for (int i = s.length() - 1; i >= 0; --i){
			if ((a + (s[i] == '-')) % 2){
				++a;
				//reverse(s.begin(), s.begin() + i + 1);
			}
		}
		/*int x;
		for 
		int a = 0, b = 0;
		for (int i = s.length() - 1; i; --i){
			if ((a + (s[i] == '-')) % 2){
				if ((a + (s[0] == '-')) % 2 == 0)
					++b;
				++a;
				reverse(s.begin(), s.begin() + i + 1);
			}
		}
		cout << a + b + (a + (s[0] == '-')) % 2 << endl;*/
		cout << a << endl;
	}
	//system("pause");
	return 0;
}