#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <iomanip>
#include <functional>

using namespace std;

#define FOR(i,c,n) for(int i=(c) ; (i)<(n) ; ++(i))
#define FR(i,n) FOR(i,0,n)

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;cin>>t;
	FR(cas,t){
		printf("Case #%d: ",cas+1);
		double c,f,x;
		cin>>c>>f>>x;
		double res=1e100;
		double sum=0;
		double rate=2;
		FR(i,10000000){
			res=min(res,sum+x/rate);
			sum+=c/rate;
			rate+=f;
		}
		cout<<fixed<<setprecision(8)<<res<<endl;
	}

}