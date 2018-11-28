#include<cstdio>
#include<set>
#include<iostream>
#include<map>
#include<cstring>
#include<iomanip>
using namespace std;
const int maxn = 20;
int x,y;
int a[maxn][maxn];
int b[maxn][maxn];
int c[maxn];
void run(double C,double F,double X){
	double ans=X*0.5;
	double s=0,tmp;
	for(int k=0;;++k){
		s += C/(2.0+k*F);
		tmp = s+X/(2.0+(k+1)*F);
		if(tmp<ans){
			ans=tmp;
		}else{
			break;
		}
	}
	cout<<ans<<endl;
}
int main(){
	ios::sync_with_stdio(false);
	cout<<fixed<<setprecision(15)<<endl;
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int T;
	cin>>T;
	for(int cas=1;cas<=T;++cas){
		double C,F,X;
		cin>>C>>F>>X;
		cout<<"Case #"<<cas<<": ";
		run(C,F,X);
	}
	return 0;
}
