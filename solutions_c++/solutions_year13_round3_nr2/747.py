#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define EPS 1e-10
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;



struct A{
	int y,x,step;
	string s;
	A(){}
	A(int y,int x,int step,string s):y(y),x(x),step(step),s(s){}
	bool operator<(const A &a)const{
		if(y!=a.y)return y<a.y;
		if(x!=a.x)return x<a.x;
		return step<a.step;
	}
};
int dy[]={1,0,-1,0};
int dx[]={0,1,0,-1};
char ch[]="NESW";


bool f(int y,int x){
	const int c=1000;
	return -c<=y&&y<=c&&-c<=x&&x<=c;
}
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T,X,Y;
	cin>>T;
	rep(i,T){
		cin>>X>>Y;
		set<A> visited;
		queue<A> q;
		A a(0,0,1,"");
		q.push(a);
		while(1){
			a=q.front();
			q.pop();
			if(a.y==Y&&a.x==X){
				cout<<"Case #"<<i+1<<": "<<a.s<<endl;
				break;
			}
			A b;
			rep(j,4){
				b.y = a.y+dy[j]*a.step;
				b.x = a.x+dx[j]*a.step;
				b.step = a.step+1;
				if(visited.find(b)==visited.end()){
					b.s = a.s+ch[j];
					visited.insert(b);
					q.push(b);
				}
			}
		}

	}
	return 0;
}