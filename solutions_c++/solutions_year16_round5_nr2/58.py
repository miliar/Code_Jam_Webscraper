#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
#include <complex>

using namespace std;
typedef long long ll;
typedef double ld;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

int n, m;
int prereq[1<<7];
vector<int> subs[1<<7];
string names;
string match[5];
int treecnt[1<<7];
int ord[1<<7];
char gen[1<<7];
ld cnt[5];
bool okay[1<<7];

void check_string(string s){
	for (int i = 0; i < m; i++){
		if (s.find(match[i]) != std::string::npos){
			cnt[i] = cnt[i] + 1.;
		}
	}
}

int main(){
	srand ( unsigned ( time(0) ) );
	
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		cin >> n;
		for (int i = 1; i <= n; i++)
			subs[i].clear();
		for (int i = 1; i <= n; i++){
			cin >> prereq[i];
			if (prereq[i] != 0){
				subs[prereq[i]].push_back(i);
			}
		}
		cin >> names;
		//cout << "names = " << names << endl;
		
		cin >> m;
		for (int i = 0; i < m; i++)
			cin >> match[i];
		
		
		memset(treecnt,0,sizeof(treecnt));	
		for (int i = 1; i <= n; i++){
			int curr = i;
			treecnt[i]++;
			while (prereq[curr] != 0){
				curr = prereq[curr];
				treecnt[curr]++;
			}
		}
		/*
		for (int i = 1; i <= n; i++)
			cout << treecnt[i] << " ";
		cout << endl;
		*/
		
		for (int i = 1; i <= n; i++)
			ord[i] = i;
		memset(gen,0,sizeof(gen));
		for (int i = 0; i < 5; i++)
			cnt[i] = 0.;
		ld trials = 50000.;
		for (int tr = 0; tr < trials; tr++){
			for (int i = 1; i <= n; i++){
				if (prereq[i] == 0){
					okay[i] = true;
				}
				else okay[i] = false;
			}
			for (int cc = 0; cc < n; cc++){
				int choice = (rand() % (n-cc)) + 1;
				int sum = 0;
				for (int i = 1; i <= n; i++){
					if (!okay[i]) continue;
					//cout << "i = " << i << ", okay[i] = " << okay[i] << endl;
					sum += treecnt[i];
					if (sum >= choice){
						okay[i] = false;
						for (int j = 0; j < subs[i].size(); j++){
							okay[subs[i][j]] = true;
							//cout << "okay[" << subs[i][j] << "] set to true" << endl;
						}
						gen[cc] = names[i-1];
						break;
					}
				}
			}	
			
			/*
			random_shuffle(ord+1,ord+n+1);
			for (int i = 1; i <= n; i++){
				if (prereq[i] == 0) continue;
				int pi = prereq[i];
				if (ord[pi] > ord[i]){
					swap(ord[pi],ord[i]);
				}
			}
			
			for (int i = 1; i <= n; i++){
				gen[ord[i]-1] = names[i-1];
				//cout << "names[i-1] = " << names[i-1] << endl;
			}
			*/
			gen[n] = 0;
			string s(gen);
			//cout << "s = " << s << endl;
			check_string(s);
		}
		cout << "Case #" << zz << ":";
		for (int i = 0; i < m; i++)
			cout << " " << (cnt[i]/trials);
		cout << endl;
	}
	
	return 0;
}
