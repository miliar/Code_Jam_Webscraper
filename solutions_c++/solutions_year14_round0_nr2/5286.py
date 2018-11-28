#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#define REP(i,m) for(int i=0;i<(m);++i)
#define REPN(i,m,in) for(int i=(in);i<(m);++i)
#define ALL(t) (t).begin(),(t).end()
#define CLR(a) memset((a),0,sizeof(a))
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
using namespace std;
static const int INF =500000000; 
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
template<class T> void chmin(T& a,const T& b) { if(a>b) a=b; }
template<class T> void chmax(T& a,const T& b) { if(a<b) a=b; }
typedef long long int lint;
typedef pair<int,int> pi;

double C,F,X;

double check(){
	double time=0,speed=2;
	while(X/speed > X/(speed+F)+C/speed){
		time+=C/speed;
		speed+=F;
	}
	return time+X/speed;
}

int main(){
	int t;cin>>t;
	REPN(setn,t+1,1){
		printf("Case #%d: ",setn);
		cin>>C>>F>>X;
		
		/*
		double lb=0,ub=100000;
		REP(hoge,60){
			double md=(lb+ub)/2;
			if(check(md)) ub=md;
			else lb=md;
		}*/

		double res=check();

		printf("%.8f\n",res);
	}



	return 0;
}



