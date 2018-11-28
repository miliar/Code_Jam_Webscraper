#include<iostream>
#include<stdio.h>
using namespace std;
double min(double a, double b){
	return ((a<b)?a:b);
}
double findBestSolution(double c, double f, double x, double cur){
	if(x/cur<c/cur+x/(cur+f))
		return x/cur;
	return c/cur+findBestSolution(c,f,x,cur+f);
}
main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		double c,x,f,ans,r;
		cin>>c>>f>>x;
		r=2.0;
		ans = findBestSolution(c,f,x,r);
		printf("Case #%d: %.7f\n", i, ans);
	}
}
