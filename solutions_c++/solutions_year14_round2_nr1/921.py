//

#include <cstdio>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <set>
#include <cmath>
#include <iostream>
#include <ctime>
#include <cassert>

using namespace std;

#define db(x) cout << #x " == " << x << endl
//#define _ << ", " <<
#define Fr(a,b,c) for( int a = b ; a < c ; ++a )
#define rF(a,b,c) for( int a = c-1 ; a >= b ; --a )
#define CL(a,b) memset(a,b,sizeof(a))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
typedef map<int,int> mii;
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3fLL
#define ULMAX 0xffffffffffffffffULL
#define y1 Y1

#define N 220

int t,n, tam[N], it[N], qts[N];
char ent[N][N], c[N];

int anda(int q){
	c[q]=ent[q][it[q]];
	int ret=0;
	while(it[q]<tam[q] && c[q]==ent[q][it[q]]) it[q]++, ret++;
	return ret;
}

int bla(){
	int ret=INF, tmp;
	Fr(i,1,120){
		tmp=0;
		Fr(j,0,n) tmp += abs(i-qts[j]);
		ret = min(ret,tmp);
	}
	return ret;
}

int main() {
//	cin.sync_with_stdio(false);
	int _=1;
	for(scanf("%d",&t);t--;){
		scanf("%d",&n);
		Fr(i,0,n) scanf("%s",ent[i]), tam[i]=strlen(ent[i]), it[i]=0;
		
		bool ok=1;
		int resp=0;
		while(it[0]<tam[0]){
			Fr(i,0,n) qts[i] = anda(i);//, printf("%c %d\n",c[i],qts[i]);
			if(qts==0) { ok=0; break; }
			Fr(i,1,n) if(c[i]!=c[i-1]){ ok=0; break; }
			resp += bla();
		}
		Fr(i,0,n) if(it[i] < tam[i]) ok=0;
		
		if(ok) printf("Case #%d: %d\n",_++,resp);
		else printf("Case #%d: Fegla Won\n",_++);
	}
	return 0;
}
