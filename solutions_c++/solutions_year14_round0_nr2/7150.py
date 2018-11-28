#include<iostream>
#include<iomanip>
#include<cstdio>
using namespace std;
main(){
int t;
cin>>t;
for(int i=0;i<t;i++){
	double c,f,x;
	cin>>c>>f>>x;
	double ans;
	ans=x/2.0;
	double time=0;
	for(int j=1;;j++){
		time = time + c/(2+(j-1)*f);
		double tempAns;
		tempAns = time + x/(2+j*f);
		if(tempAns < ans){
		ans = tempAns;
		}
		else
		break;
	}
	printf("Case #%d: %.7f\n",i+1,ans);
}
}