
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <cassert>

using namespace std;

char s[10][20];
int r[10];
int c[10];

set<string> h;

int mymax;
int mycount;

int sch(int lev, int m, int n){

	int mysize;

	if(lev == m){
		
		for(int i=0; i<n; ++i){
			if(c[i] == 0){
				return 0;
			}
		}
		mysize = 0;
		for(int i=0; i<n; ++i){
			h.clear();
			for(int j=0; j<m; ++j){
				if(r[j] == i){
					//printf("%s\n", s[j]);
					int len = strlen(s[j]);
					for(int k=0; k<=len; ++k){
						h.insert(string(s[j], s[j]+k));
					}
				}
			}
			assert(h.size() != 0);
			/*	
			cout << "====" << endl;
			for(set<string>::iterator ite = h.begin(); ite != h.end(); ++ite){
				cout << *ite << " ";
			}
			cout << "~~~" << h.size() << endl << endl;
			*/
			mysize += h.size();
		}

		if(mysize == mymax){
			mycount ++;
		}

		if(mysize > mymax){
			mymax = mysize;
			mycount = 1;
		}

		return 0;
	}

	for(int i=0; i<n; ++i){
		r[lev] = i;
		c[i] ++;
		sch(lev+1, m, n);
		c[i] --;
	}

	return 0;
}

int main(){
	
	int testcase; scanf("%d", &testcase);
	int m, n;

	for(int t=1; t<=testcase; ++t){
		scanf("%d %d", &m, &n);
		for(int i=0; i<m; ++i){
			scanf("%s", s[i]);
		}
		mymax = -1;
		mycount = 0;
		memset(r, 0, sizeof(r));
		memset(c, 0, sizeof(c));
		sch(0, m, n);
		printf("Case #%d: %d %d\n", t, mymax, mycount);
	}
	return 0;
}
