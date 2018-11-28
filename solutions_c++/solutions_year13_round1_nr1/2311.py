#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<=(int)(m);i++)
using namespace std;
int T,t,r;
int main(){
freopen("A-small-attempt0.in","rt",stdin);
freopen("A-small-attempt0.out","wt",stdout);
cin >> T;
rep(tt,T){
	cin >>r>>t;
	int b=0,z,x=0,y=1;
	while(t>=1)
		{
		z=(pow(r+y,2)-pow(r+x,2));
		t=t-z;if(t>=0){b++;x+=2;y+=2;}else break;

		}
	cout<<"Case #"<<(tt+1)<<": "<<b<<"\n";
	}
}
