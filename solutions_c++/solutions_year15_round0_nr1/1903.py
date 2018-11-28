#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <cstring>

using namespace std;
#define clr(A) memset(A,0,sizeof(A))


typedef long long LL;
typedef unsigned long long ULL;

typedef pair<int,int> P;
const int INF = 1000000009;
const int mm = 10005;


int main(){
//    freopen("wcbao.in","r",stdin);
//    freopen("wcbao.out","w",stdout);
    int T,c = 0;
    cin >> T;
    char st[mm];
    while(T--){
        int L;
    	scanf("%d%s",&L,st);
    	int ans = 0,pep = 0;
    	for(int i = 0; st[i] != '\0'; i++)
    	if(st[i] != '0'){
    		int need = max(0,i-pep);
    		ans += need;
    		pep += need + st[i] - '0';
    	}
    	printf("Case #%d: %d\n",++c,ans);
//    	cout << ans << endl;
    }
    return 0;
}
