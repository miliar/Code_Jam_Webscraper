#include<iostream>
#include<cstdio>
using namespace std;

double timef(double c, double f, double max, double r, double t) {
	if (max/(r+f)>(max-c)/r) return (t+max/r);
	else return timef(c, f, max, r+f, t+c/r);
}
int main() {
	int cases;cin>>cases;
	for(int i=0;i<cases;i++) {
		double c, f, max;
		cin>>c;cin>>f;cin>>max;
		cout<<"Case #"<<i+1<<": ";
		printf("%.17g\n", timef(c,f,max,2.0,0.0));cout<<endl;
		}
}
