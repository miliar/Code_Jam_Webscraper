#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X));
#define xx first
#define yy second
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

typedef pair<bool, char> pbc;


pbc multi( pbc a, pbc b) {
	bool signal = (a.first==b.first) ? 0 : 1;
	char resp;
	if(a.second == '1') {resp = b.second;}
	else if(b.second == '1') {resp = a.second;} 
	else if(a.second == b.second) {
		resp = '1';
		if(a.second != '1') {signal = 1 - signal;}
	} else if(a.second == 'i') {
		if(b.second == 'j') {
			resp = 'k';
		} else if(b.second == 'k') {
			resp = 'j';
			signal = 1 - signal;
		}
	} else if(a.second == 'j') {
		if(b.second == 'i') {
			resp = 'k';
			signal = 1 - signal;
		} else if(b.second == 'k') {
			resp = 'i';
		}
	} else if(a.second == 'k') {
		if(b.second == 'i') {
			resp = 'j';
		} else if(b.second == 'j') {
			resp = 'i';
			signal = 1 - signal;
		}
	}
	return make_pair(signal, resp);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		int l, x, state=0;
		char s[10010];
		pbc cur = make_pair(false, '1');
		scanf("%d %d %s", &l, &x, s);

		while(x--){
			for(int i =0; i<l;i++) {
				char c = s[i];
				cur = multi(cur, make_pair(false,c));
				if(cur.first == false &&
					 ((state==0 && cur.second == 'i') ||
						(state==1 && cur.second == 'j') ||
						(state==2 && cur.second == 'k'))) {
					state++;
					cur = make_pair(false, '1');
				}
				/*
				printf("c:%c state:%d cur.first:%d cur.second:%c\n", 
						c,state,cur.first,cur.second);
				*/
			}
		}
		if(state==3 && cur.first == false && cur.second == '1') 
			printf("Case #%d: YES\n",caso);
		else printf("Case #%d: NO\n",caso);
	}
	return 0;
}
