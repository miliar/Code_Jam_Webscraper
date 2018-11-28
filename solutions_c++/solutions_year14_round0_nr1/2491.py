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

int n, ns[10][10],t;
bool bla[20];

void ble(){
	scanf("%d",&n), n--;
	Fr(i,0,4) Fr(j,0,4){
		scanf("%d",&ns[i][j]);
		if(i!=n) bla[ns[i][j]]=false;
	}
}

int main() {
//	cin.sync_with_stdio(false);
	int _=1;
	for(scanf("%d",&t);t;t--){
		CL(bla,1);
		ble(), ble();
		int resp=-1;
		Fr(i,1,17) if(bla[i]){
			if(resp==-1) resp=i;
			else resp=-2;
		}
		printf("Case #%d: ",_++);
		if(resp==-1) puts("Volunteer cheated!");
		else if(resp==-2) puts("Bad magician!");
		else printf("%d\n",resp);
	}
	return 0;
}
