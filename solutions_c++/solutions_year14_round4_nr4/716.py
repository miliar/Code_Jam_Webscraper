///SACAR FREOPEN.
#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<list>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<stack>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<map>
#include<sstream>
#include<assert.h>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define forn(i,n) for(int i=0; i<(int)n; i++)
#define dforn(i,n) for(int i=(int)n-1; i>=0; i--)
#define formn(i,m,n) for(int i=m; i<(int)n; i++)
#define dformn(i,m,n) for(int i=n-1; i>=m; i--)
#define mp make_pair
#define pb push_back

const double PI=acos(-1.0);

typedef long long tint;
typedef pair<int,int> pint;

int m,n;
string s[10];
int aRes;

struct Trie{
	map<char,Trie> children;
};

void insert(Trie* t, string & s){
	forn(i,s.size()){
		if(!((t -> children).count(s[i])))
			aRes++;
		t = &(t -> children[s[i]]);
	}
}

int main(){
freopen("C.in","r",stdin);
freopen("C.out","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1; tc <= TC; tc++){
		map<int,int> times;
		cin >> m >> n;
		for(int i = 0; i < m; i++)
			cin >> s[i];
		for(int mask = 0; mask < ((1<<(2 * m)) - 1); mask++){
			int where[8];
			for(int i = 0; i < m; i++){
				where[i] = ((mask >> (2 * i)) & 3);
			}
			bool belowN = true;
			set<int> have;
			for(int i = 0; i < m; i++){
				have.insert(where[i]);
				if(where[i] >= n)
					belowN = false;
			}
			if(belowN == false)
				continue;
			///ahora hago la cuenta con esto.
			Trie t[n];
			///los tiro en el trie
			aRes = have.size();///por los nodos raiz
			for(int i = 0; i < m; i++){
				insert(& t[where[i]], s[i]);
			}
			times[aRes]++;
		}
		map<int,int> :: iterator it = times.end();
		it--;
		int X = (*it).first;
		int aps = (*it).second;
		cout << "Case #" << tc << ": " << X << " " << aps << endl;
	}
    return 0;
}
