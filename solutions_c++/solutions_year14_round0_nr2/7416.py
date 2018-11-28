#include<iostream>
#include<cstdio>
using namespace std;
int T;
double C,F,X;
double solve();
int main()
{
	int i;
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt0-2.out","w",stdout);
	cin>>T;
	for(i=1;i<=T;i++){
		cin>>C>>F>>X;
		printf("Case #%d: %.8f\n",i,solve());
	}
	return 0;
}
double solve()
{
	double mt,t1,t2,p=2.0;
	if(X<=C)return X/p;
	mt=X/p;
	t1=0.0;
	while(t1<mt){
		t1+=C/p;
		t2=t1+X/(p+F);
		if(t2<mt)mt=t2;
		p+=F;
	}
	return mt;
}
