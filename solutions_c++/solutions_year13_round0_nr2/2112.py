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
#define MAY 100100
#define INF 100000000
#define MOD 1000000007
#define PI 3.141592654
typedef long long LL;
typedef double D;
#define G(x) (D)(x)
#define F(x) (LL)(x)

int a[110][110], r[110][110], N,M;

int main(){
    int T;
    cin>>T;
    FOR(t,1,T+1){
        cin>>N>>M;
        mem(a,0);
        FOR(i,1,N+1)FOR(j,1,M+1){
            cin>>a[i][j];
            a[i][0]=max(a[i][0],a[i][j]);
            a[0][j]=max(a[0][j],a[i][j]);
        }
        FOR(i,0,N+1)FOR(j,0,M+1)r[i][j]=100;

        FOR(y,1,M+1)FOR(i,1,N+1)r[i][y]=min(r[i][y],a[0][y]);
        FOR(x,1,N+1)FOR(j,1,M+1)r[x][j]=min(r[x][j],a[x][0]);

        int res=1;
        FOR(i,1,N+1){
            if(!res)break;
            FOR(j,1,M+1)if(a[i][j]!=r[i][j])res=0;
        }
        cout<<"Case #"<<t<<": "<<(res?"YES":"NO")<<endl;

    }
    return 0;
}

