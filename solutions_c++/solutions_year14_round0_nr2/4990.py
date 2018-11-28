#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <algorithm>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SET(v,x) memset(v,x,sizeof v)
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++)
#define EACH(it,v) for(typeof((v).begin()) it = (v).begin();it!=(v).end();it++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define SZ(v) int(v.size())
#define SI ({int x;scanf("%d",&x);x;})




	int main(){

    freopen("A-small-practice.in", "rt", stdin);
    freopen("A-small.out", "wt", stdout);
    int t;
	cin>>t;
	int count=0;
	while(t--){
		double C,F,X,y=0;
		int n=0;
		count++;
		cin>>C>>F>>X;
			double ny,temp=0;
			y = temp + (X/(2+(n*F)));
			temp =  C/(2+(n*F));
			ny= temp + (X/(2+((n+1)*F)));
			while(ny<y){
				n++;
				y = temp + (X/(2+(n*F)));
				temp = temp + (C/(2+(n*F)));
				ny= temp + (X/(2+((n+1)*F)));
			}
		cout<<"case #"<<count<<": ";
			printf("%.7lf\n",y);
	}
	return 0;
}
