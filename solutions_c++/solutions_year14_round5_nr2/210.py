#include <iostream>
//#include <vector>
#include <cstring>

using namespace std;

//typedef vector<int> vi;

static int n,p,q;
//vi hp;
static int hp[101];
//vi val;
static int val[101];
//int mem[105][205][20005][2];
static int mem[101][201][20001];

//int calc(int curr,int leftHp,int reserve,int isMyTurn);
static int calc(const int &curr,const int &leftHp,const int &reserve);
static inline int maxInt(const int &a,const int &b);

int main() {
	int cases;
	cin>>cases;
	for(int round=1; round<=cases; round++) {
		cin>>p>>q>>n;
		//hp.resize(n);
		//val.resize(n);
		for(int i=0; i<n; i++)
			cin>>hp[i]>>val[i];
		//mem.assign(n,vvi(20005,vi(2,-1)));
		memset(mem,-1,sizeof mem);
		cout<<"Case #"<<round<<": "<<calc(0,hp[0],1)<<'\n';
	}
	return 0;
}

//int calc(int curr,int leftHp,int reserve,int isMyTurn) {
static int calc(const int &curr,const int &leftHp,const int &reserve) {
	if(curr>=n)
		return 0;
	//if(leftHp<0)
	//	return calc(curr,0,reserve,isMyTurn);
	//int &ans=mem[curr][leftHp][reserve][isMyTurn];
	int &ans=mem[curr][leftHp][reserve];
	if(ans!=-1)
		return ans;
	ans=0;
	if(reserve>0) {
		const int &nextHp=leftHp-p;
		if(nextHp<=0)
			ans=maxInt(ans,val[curr]+calc(curr+1,hp[curr+1],reserve-1));
		else
			ans=maxInt(ans,calc(curr,nextHp,reserve-1));
	}
	const int &nextHp=leftHp-q;
	if(nextHp<=0)
		ans=maxInt(ans,calc(curr+1,hp[curr+1],reserve+1));
	else
		ans=maxInt(ans,calc(curr,nextHp,reserve+1));
	return ans;
}

static inline int maxInt(const int &a,const int &b) {
	return (a<b)?b:a;
}
