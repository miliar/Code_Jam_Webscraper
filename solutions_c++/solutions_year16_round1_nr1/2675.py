#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#define FOR(i,a,b) for (int i = a; i <= b; i++)
#define FORN(i,N) for (int i = 0; i < N; i++)
#define FORD(i,a,b) for (int i = a; i >= b; i--)


using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

int main() {

	char temp[10000];
	string s1;

	int T;
	scanf("%d",&T);
	FOR(c,1,T) {
		scanf("%s",temp);
		s1 = "";
		s1 += temp[0];
		FOR(i,1,strlen(temp)-1) {
				if(temp[i] >= s1[0])
					s1 = temp[i] + s1;
				else
					s1 += temp[i];
		}
		cout << "Case #"<< c <<": " << s1 << endl;
	}

	return 0;
}
