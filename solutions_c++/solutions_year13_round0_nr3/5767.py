#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <fstream>

using namespace std;

#define DEBUG(x) cout<< #x << ':' << x << endl
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define REP(i,n) FOR(i,0,n-1)
#define FORIT(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define SZ(a) (int)(a).size()
#define ALL(a) (a).begin(), (a).end()
#define ZERO(a) memset(a, 0, sizeof(a))
#define PB push_back
#define MP make_pair
#define LEN(a) (int)(sizeof(a) / sizeof(a[0]))
#define abs(x) (((x)^((x)>>31))-((x)>>31))
const int inf = ~0u>>1;

typedef long long ll;

void tprint(int ii, int res){
	printf("Case #%d: %d\n",ii,res);
}

bool check(int a){
	int aa;
	stringstream ss;
	string sa,rsa;
	ss << a;
	ss >> sa;
	rsa = sa;
	reverse(ALL(rsa));
	ss.clear();
	ss << rsa;
	ss >> aa;
	if (aa == a) return true;
	else return false;
}

int main()
{
	int T;
	cin>>T;
	int a,b;
	FOR(ii,1,T){
		scanf("%d%d",&a,&b);
//		cout<<check(16)<<endl;
		int sqa = (int)sqrt(a);
		int ant = 0;
		for(int i=sqa; i*i <= b; i++){
			if (i*i < a) continue;
			if (check(i) && check(i*i))
				ant++;
		}
		tprint(ii,ant);
	}
	return 0;
}
