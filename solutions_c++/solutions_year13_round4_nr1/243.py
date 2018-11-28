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
__int64 price(__int64 n,__int64 k){
	__int64 ans=((((__int64)2*n-k+1)*k)/2);
	ans=ans%1000002013;
	return ans;
}
struct node{
	int tt;
	int p;
};
bool big(node a,node b){
	return a.tt<b.tt;
}
__int64  judge(){
	__int64 ans=0;
	__int64 old=0,novel=0;
	int n,m;
	scanf("%d%d",&n,&m);
	vector<node> in(m),out(m);

	REP(i,m){
		int a,b,c;
		scanf("%d%d%d",&a,&b,&c);
		in[i].tt=a;
		out[i].tt=b;
		in[i].p=out[i].p=c;
		old+=c*price(n,b-a);
		old=old%1000002013;
	}
	sort(ALL(in),big);
	sort(ALL(out),big);
	
	vector<pair<int,int > > tikes;
	int j=0;
	REP(i,in.size()){
		
		while(out[j].tt<in[i].tt){
			int num=out[j].p;
			while(num>0){
				int s=tikes.back().first;
				
				if(tikes.back().second>num){
					tikes.back().second-=num;
					novel+=num*price(n,out[j].tt-s);
					novel=novel%1000002013;
					num=0;
				}
				else{
					
					novel+=tikes.back().second*price(n,out[j].tt-s);
					novel=novel%1000002013;
					num-=tikes.back().second;
					tikes.pop_back();
				}
			}
			j++;
		}
		tikes.push_back(MP(in[i].tt,in[i].p));
	}
		
	while(j<m){
		int num=out[j].p;
		while(num>0){
			int s=tikes.back().first;
				
			if(tikes.back().second>num){
				tikes.back().second-=num;
				novel+=num*price(n,out[j].tt-s);
				novel=novel%1000002013;
				num=0;
			}
			else{
					
				novel+=tikes.back().second*price(n,out[j].tt-s);
				novel=novel%1000002013;
				num-=tikes.back().second;
				tikes.pop_back();
			}
		}
		j++;
	}

	ans=old-novel;
	if(ans<0)ans+=1000002013;
	return ans;
}


int main(){
	int t;
	scanf("%d",&t);
	REP(tt,t){
		__int64 ans=judge();
		printf("Case #%d: %I64d\n",tt+1,ans);
	}




	return 1;



}