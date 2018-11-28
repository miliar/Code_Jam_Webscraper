// fbhc.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

// fbhc.cpp : Defines the entry point for the console application.
//



#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<limits>
#include<climits>
#include<cmath>
#include<functional>
#include<ctime>
#include<cstdlib>
#include<fstream>
#include<typeinfo>
using namespace std;

#define ff first
#define ss second
typedef long long int ll;
typedef short int i16;
typedef unsigned long long int u64;
typedef unsigned int u32;
typedef unsigned short int u16;
typedef unsigned char u8;

vector<int> e;

int solve(int a, int b) {

	return 0;
}
int maint()
{
	ofstream cout("out.txt");
	ifstream cin("g.in");

	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {


		int n;
		cin >> n;
		vector<int> a(n);

		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		e = a;
		cout << "Case #" << tc << ": ";
		string ans = "";
		while (1){

			int f = 0;
			for (int i = 0; i < n; i++){

				if (a[i]) { f = 1; break; }
			}
			ans += " ";
			if (!f) break;
			int m = 0, mind = -1;
			vector<int> d = a;
			sort(d.begin(), d.end());
			if (d.size() >= 2 && 0){

				if (d.back() == d[n - 2]) {

					int x = -1, y = -1, m = 0;
					for (int i = 0; i < n; i++) {

						if (a[i] > m) {

							x = i;
							m = a[i];
						}
					}
					for (int i = 0; i < n; i++) {

						if (a[i] == m && x != i) {

							y = i;
						
						}
					}

					char c = x + 'A';
					
					ans += c;
					c = y + 'A';
					ans +=  c;
					a[x]--;
					a[y]--;
					continue;
				}
			}
			for (int i = 0; i < n; i++) {


				
				if (a[i] > m) {

					
					a[i]--;
					vector<int> b = a;
					sort(b.begin(), b.end());
					reverse(b.begin(), b.end());
					int t = 0;
					for (int j = 0; j < n; j++) {
						t += a[j];

					}
					if (t < b[0] * 2) {
						a[i]++;
						continue;
					}
					m = a[i];
					mind = i;
					a[i]++;
				}

			}
			if (mind == -1) {

				if (d.size() >= 2 ) {

					int x = -1, y = -1, m = 0;
					for (int i = 0; i < n; i++) {

						if (a[i] > m) {

							x = i;
							m = a[i];
						}
					}
					int mm = 0;
					for (int i = 0; i < n; i++) {

						if (a[i] > mm && x != i) {

							mm = a[i];
							y = i;
							
						}
					}

					char c = x + 'A';
					ans +=  c;
					if (y >= 0){
						c = y + 'A';
						ans += c;
					}
					a[x]--;
					if (y>=0)
					a[y]--;
					continue;
				}
			}
			
			char c = mind + 'A';
			ans += c;
			a[mind]--;
			m = 0, mind = -1;
			for (int i = 0; i < n; i++) {

				if (a[i] > m) {

					
					a[i]--;
					vector<int> b = a;
					sort(b.begin(), b.end());
					reverse(b.begin(), b.end());
					int t = 0;
					for (int j = 0; j < n; j++) {
						t += a[j];

					}
					if (t < b[0] * 2) {
						a[i]++;
						continue;
					}
					m = a[i];
					mind = i;
					a[i]++;
				}
				

				//a[mind]--;
			}
			//ans += " ";
			if (mind == -1) continue;
			 c = mind + 'A';
			ans += c;
			a[mind]--;
			m = 0, mind = -1;
		}
		cout << ans.substr(1);
		cout << '\n';
	}

	return 0;
}




int _tmain(int argc, _TCHAR* argv[])
{
	return maint();
	return 0;
}

