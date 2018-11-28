#include<iostream>
#include<cstdio>
#include<iomanip>
#include<cstring>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;cin>>T;int cas=0;
	while(T--){
		double C,F,X;
		cin>>C>>F>>X;
		double mintime=1.0*X/2.0;
		for(int i=1;;i++){
			double tm=0.0;
			for(int j=1;j<=i;j++){
				tm+=1.0*C/(1.0*(j-1)*F+2.0);
			}
			tm+=X/(1.0*i*F+2.0);
			if(tm<=mintime){
				mintime=tm;
			}else break;
		}
		cout<<"Case #"<<++cas<<": ";
		cout<<fixed<<setprecision(7)<<mintime<<endl;
	}
	return 0;
}