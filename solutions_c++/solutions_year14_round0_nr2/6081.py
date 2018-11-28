#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
#define maxN 1000000
double sum[maxN];
int main(){
	int casos; cin>>casos;
	int a1,a2;
	for(int caso=1;caso<=casos;caso++){
		double C,F,X; cin>>C>>F>>X;
		double ans=1e30;
		double tmp1=0.0;
		for(int n=0;n<maxN;n++){
			double tmp2=tmp1+X/(2.0+n*F);
		//	cout<<n<<" "<<tmp2<<endl;
			ans=min(tmp2,ans);
			tmp1=tmp1+C/(2+n*F);
		}
		printf("Case #%d: %.6f\n",caso,ans);
		
	}
return 0;}
