#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<bitset>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<cstring>
#include<sstream>
#include<climits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define S(x) scanf("%d",&x)
#define SD(x) scanf("%lf",&x)
#define SL(x) scanf("%lld",&x)
#define pb(x) push_back(x)
#define mp make_pair
#define F(i, a, b) for (int i = int(a); i < int(b); i++)
#define forit(it, a) for (it = (a).begin(); it != (a).end(); it++)
#define M(x,i) memset(x,i,sizeof(x))

/* -------------------CODE GOES HERE---------------------- */

pair<int, char> mult(char a, char b){

	if(a == '1'){

		if(b == '1') return mp(1, '1');
		if(b == 'i') return mp(1, 'i');
		if(b == 'j') return mp(1, 'j');
		if(b == 'k') return mp(1, 'k');
	}

	if(a == 'i'){

		if(b == '1') return mp(1, 'i');
		if(b == 'i') return mp(-1, '1');
		if(b == 'j') return mp(1, 'k');
		if(b == 'k') return mp(-1, 'j');
	}

	if(a == 'j'){

		if(b == '1') return mp(1, 'j');
		if(b == 'i') return mp(-1, 'k');
		if(b == 'j') return mp(-1, '1');
		if(b == 'k') return mp(1, 'i');
	}

	if(a == 'k'){

		if(b == '1') return mp(1, 'k');
		if(b == 'i') return mp(1, 'j');
		if(b == 'j') return mp(-1, 'i');
		if(b == 'k') return mp(-1, '1');
	}
}

int main(){
	
	int T, L, X; S(T);

	string str;
	int tst = 1;
	bool ans, poss[2];

	pair<int, char> prev, curr;

	while(T--){

		ans = false;
		M(poss, false);
		prev = mp(1, '1');

		S(L); S(X);
		cin>>str;

		F(x,0,X){
			
			F(y,0,L){

				curr = mult(prev.second, str[y]);
				curr.first *= prev.first;
				prev = curr;

				if((curr.first == 1) && (curr.second == 'i')) poss[0] = true;
				if((curr.first == 1) && (curr.second == 'k') && (poss[0])) poss[1] = true;
			}
		}
		
		if((curr.first == -1) && (curr.second == '1') && (poss[0]) && (poss[1])) ans = true;

		printf("Case #%d: %s\n", tst++, (ans ? "YES" : "NO"));
	}
}