/*
 *Author:       Zhaofa Fang
 *Created time: 2013-04-13-10.50
 *Language:     C++
 */
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define DEBUG(x) cout<< #x << ':' << x << endl
#define FOR(i,s,t) for(int i = (s);i <= (t);i++)
#define FORD(i,s,t) for(int i = (s);i >= (t);i--)
#define REP(i,n) FOR(i,0,n-1)
#define REPD(i,n) FORD(i,n-1,0)
#define PII pair<int,int>
#define PB push_back
#define MP make_pair
#define ft first
#define sd second
#define lowbit(x) (x&(-x))
#define INF (1<<30)


bool check(int x){
    vector<int>vec;
    int tmp=x;
    while(tmp>0){
        vec.PB(tmp%10);
        tmp/=10;
    }
    tmp = x;
    REPD(i,vec.size()){
        if(tmp%10!=vec[i])return false;
        tmp/=10;
    }
    return true;

}
int fun(int x){
    int cnt = 0;
    for(int i=1;i*i<=x;i++){
        if(check(i)&&check(i*i))cnt++;
    }
    return cnt;
}

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	cin>>T;
	FOR(cas,1,T){
        int A,B;
        scanf("%d%d",&A,&B);
        int ans = fun(B)-fun(A-1);

        printf("Case #%d: ",cas);
        printf("%d\n",ans);

	}
	return 0;
}
