#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
struct node{
	double kur,sn,yap;
	node(double _b,double _c,double _d){
		kur=_b;
		sn=_c;
		yap=_d;
	}
	friend bool operator < (const node &a,const node &b){return a.sn>b.sn;}
};
int n;
double a,b,c;
double bfs(){
	priority_queue <node> q;
	q.push(node(0,0,2));
	double x,y,z,mis=99999999999.99999;
	while(!q.empty()){
		x=q.top().kur;
		y=q.top().sn;
		z=q.top().yap;
		q.pop();
		if(y>=mis) return mis;
		q.push(node(0,y+(a-x)/z,z+b));
		mis=min(mis,y+(c-x)/z);
		//~ q.push(node(c,y+(c-x)/z,z));
	}
}
int main()
{
	scanf(" %d",&n);
	for(int i=1;i<=n;i++){
		scanf(" %lf %lf %lf",&a,&b,&c);
		printf("Case #%d: %.7lf\n",i,bfs());
	}
	return 0;
}
