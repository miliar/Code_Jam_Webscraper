#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue> 
#include <algorithm>
#include <bitset>
#include <set>

using namespace std;

#define REP(i,n) for(long long int i = 0; i < int(n); ++i)
#define REPV(i, n) for (long long int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(long long int i = (int)(a); i < (int)(b); ++i)

#define ALL(v) (v).begin(), (v).end()
#define PF push_front
#define PB push_back
#define MP make_pair
#define F first
#define S second

#define lli long long int

int x;
int yy;

char str[1000];

struct attac {
	int d;
	int w, e;
	int s;
};

int wall[1100];

int main()
{
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif	
	int T;
	cin >> T;
	REP(q, T) {		
		cout << "Case #" << (q + 1) << ": ";
		
		int k = 0;
		attac *a = new attac[110];

		int n;
		cin >> n;
		vector<pair<int, int> > vSort;
		REP(j, n) {		
			int di, ni, wi, ei, si, d_di, d_pi, d_si;
			cin >> di >> ni >> wi >> ei >> si >> d_di >> d_pi >> d_si;
			ei += 500;
			wi += 500;
			REP(i, ni) {
				a[k].s = si;
				a[k].d  = di;
				a[k].w = wi;
				a[k].e = ei;

				vSort.push_back(MP(di, k));

				wi += d_pi;
				ei += d_pi;
				di += d_di;
				si += d_si;
				++k;
			}
		}
		

		std::sort(ALL(vSort));
		REP(iii, 850) {
			wall[iii] = 0;
		} 

		int i = 0;
		int count = 0;
		while (i < vSort.size()) {
			int s = i;
			int d = a[vSort[i].second].d;
			//успешные атаки
			while(i < vSort.size() && a[vSort[i].second].d == d) {
				attac att =a[vSort[i].second];
				for(int i = att.w; i < att.e; ++i) {
					if (wall[i] < att.s) {
						count++; 
						break;
					}
				}
				++i;
			}
			i = s;
			//застроить стену
			while(i < vSort.size() && a[vSort[i].second].d == d) {
				attac att =a[vSort[i].second];
				for(int i = att.w; i < att.e; ++i) {
					wall[i] = max(wall[i], att.s);
				}
				++i;
			}
		}

		cout << count << endl;
	}
    return 0;
}