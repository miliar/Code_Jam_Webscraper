#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <cmath>
#include <stack>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <cassert>
#include <iomanip>
using namespace std;
#define pb push_back
#define FOR(i,ini,fin) for(int i=(int)ini;i<(int)fin;i++)
#define FOR_INC(i,ini,fin,inc) for(int i=(int)ini;i<(int)fin;i+=inc)
#define FOR_IT(iter,C) for(typeof(C.begin()) iter = C.begin();iter!=C.end();iter++)
#define all(A) A.begin(), A.end()
#define mem(x,val) memset(x,val,sizeof(x))
#define EPS 1e-7
#define MAY 1000005
#define INF 100000000
#define MOD 1000000007
#define PI 3.141592654
typedef long long LL;
#define F(x) (LL)(x)
typedef double D;
#define G(x) (D)(x)

int T,E,R,N,v[12];
int res;
void get(int pos, int e,int gain){
    res=max(res,gain);
    if(pos>=N)return;
    FOR(x,0,e+1){
        int new_gain=gain+(x*v[pos]);
        get(pos+1,min(E,e-x+R), new_gain);
    }
}
int main(){
    cin>>T;
    FOR(t,1,T+1){
        cin>>E>>R>>N;
        FOR(i,0,N)cin>>v[i];
        res=0;
        get(0,E,0);
        printf("Case #%d: %d\n",t,res);
    }
    return 0;
}
