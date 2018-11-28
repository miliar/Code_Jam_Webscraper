#pragma comment(linker, "/STACK:1234567890000")

#include<iostream>
#include<iomanip>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<set>

#define Author "DemoVersion"
using namespace std;
int dx[]={0,0,-1,1,1,-1,1,-1};
int dy[]={1,-1,0,0,1,1,-1,-1};
typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;

int main(){

    ios_base::sync_with_stdio(0);

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

	ll P,Q,T,z,val,B;
	val=1ll<<40;
	double a,b;
	char Ti;
	int out;
	cin>>T;
	for(z=1;z<=T;z++){
		cout<<"Case #"<<z<<": ";
		cin>>P>>Ti>>Q;
		a=(double)val/Q;
		b=(double)P*a;
		if(b!=floor(b)){
			cout<<"impossible";
		}else{
			double a=(double)P/Q;
			double b=1;
			int out=0;
			while(a<b){
				b/=2;
				out++;
			}
			cout<<out;
		}
		cout<<endl;
	}
	return 0;
}
