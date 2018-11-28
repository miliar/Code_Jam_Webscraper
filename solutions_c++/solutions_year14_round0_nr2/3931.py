#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin>>T;
	rep(i,T){
		double c,f,x;
		cin>>c>>f>>x;
		double ans=x/2;
		double pret=0;
		for(int j=1;j<100000;j++){
			double t=pret + c/(2+(j-1)*f);
			pret=t;
			t+=x/(2+f*j);
			ans=min(ans,t);
		}
		//cout<<"Case #"<<i+1<<": "<<ans<<endl; 
		printf("Case #%d: %.6f\n",i+1,ans);
	}
	return 0;
}