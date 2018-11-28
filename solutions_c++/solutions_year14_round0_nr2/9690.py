#include<bits/stdc++.h>
using namespace std;
double C,X,F;
double cost(int k){
	double res=0;
	for(int i=0;i<k;i++)
		res+=(C/(2.0+i*F)*1.0);
	res+=(X/(2.0+(k)*F)*1.0);
	return res;
}
int main(){
	int t;
	cin >> t;
	for(int ii=1;ii<=t;ii++){
		cin >> C >> F >> X;
		cout << "Case #" << ii<<": " ;
		int k=1;
		double c1=cost(1);
		double ans=cost(0);
		while((ans-c1)>=1e-7){
			k++;
			ans=c1;
			c1=cost(k);
		}
		printf("%.7lf\n",ans);
	}
}
