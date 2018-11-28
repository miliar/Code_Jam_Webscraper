#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

//YOLO
//code by loyolman

using namespace std;

struct node {
	double flow=0.0;
	double tmp=0.0;
};

node mix(node a, node b) {
	node c;
	c.flow=a.flow+b.flow;
	c.tmp=(a.flow)*(a.tmp)+(b.flow)*(b.tmp);
	c.tmp=c.tmp/c.flow;
	
	return c;
}

double mmax (double a, double b) {
	if (a>b) return a;
	else return b;
}

int main() {
	int T;
	cin>>T;
	for (int j=1;j<=T;j++) {
		cout<<fixed;
		//cout<<std::setprecision(7);
		cout<<"Case #"<<j<<": ";
		int N;
		bool possible=false;
		node target,cool,hot,next;
		cin>>N>>target.flow>>target.tmp;
		
		for (int i=0;i<N;i++) {
			node a;
			cin>>a.flow>>a.tmp;
			
			if (a.tmp==target.tmp) next=mix(a,next);
			
			if (a.tmp>=target.tmp) hot=mix(hot,a);
			else cool=mix(cool,a);
		}
		
		if (cool.flow==0.0) {
			if (next.flow!=0.0) {
				double ans=target.flow/next.flow;
				cout<<ans<<endl;
			}
			else cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if (hot.flow==0.0) {
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		} 
		if (hot.tmp==target.tmp) {
			double ans=target.flow/hot.flow;
			cout<<ans<<endl;
			continue;
		}
		
		double a;//some magic on my paper. hope it will work
		a=(target.tmp-cool.tmp)/(hot.tmp-target.tmp);
		double x=target.flow/(a+1);
		//hot water = a*x cool water = x (flow)
		
		double time_cool=x/cool.flow;
		double time_hot=(a*x)/hot.flow;
		double ans=mmax(time_cool, time_hot);
		
		cout<<ans<<endl;
		
	}
	return 0;
}
