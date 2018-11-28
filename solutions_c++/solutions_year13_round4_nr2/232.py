#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <iomanip> 
#include <vector>
#include <list>
#include <utility> 
#include <iterator> 
#include <math.h> 
#include <algorithm> 
#include <stdio.h> 
using namespace std;
#define REP(i,T) for(int i=0;i<T;++i)
#define MP make_pair
#define PII pair<int,int>
#define BG begin
#define ND end
#define VI vector<int>
#define VB vector<bool>
#define ALL(i) i.BG(),i.ND()
#define FORI(i,a,b) for(int i=a;i<b;++i)
#define OUT(i) while(!i.empty())
#define GP(a,b) a[b.first][b.second]
#define EX(a,b) (a.find(b)!=a.end())

__int64  judge(int t){
	__int64 n,m;
	scanf("%I64d%I64d",&n,&m);
	__int64 x=m-1;
	if(m==((__int64)1)<<n){
		
		printf("Case #%d: %I64d %I64d\n",t,m-1,m-1);
		return 0;

	}
	vector<int> s(n);
	__int64 hm=1;
	int fb,fk;
	REP(i,n){
		s[i]=(x&hm)>0;
		hm=hm<<1;
		if(s[i]==0)fb=i;
	}
	__int64 a,b;
	__int64 tmp=1;
	a=1;
	REP(i,n-fb-1){
		tmp=tmp<<1;
		a+=tmp;
	}
	--a;
	
	x=m;
	hm=1;
	REP(i,n){
		s[i]=(x&hm)>0;
		hm=hm<<1;
		if(s[i]==1)fk=i;
	}
	b=0;
	REP(i,n){
		b=b<<1;
		b+=(fk>0);
		fk--;
	}
	printf("Case #%d: %I64d %I64d\n",t,a,b);
	return 0;
}


int main(){
	int t;
	scanf("%d",&t);
	REP(tt,t){
		__int64 ans=judge(tt+1);
		//printf("Case #%d: %I64d\n",tt+1,ans);
	}




	return 1;



}