#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cassert>
#include<vector>
#include<string>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<bitset>
#include<cstdio>
#include<cmath>
#include<climits>
#include<ctime>
#include<string>
#include<fstream>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#define ip(x) scanf("%d",&x)
#define ipLL(x) scanf("%lld",&x)
#define ForInc(var,beg,end) for(int var=beg;var<=end;++var)
#define advForInc(var,beg,end,inc) for(int var=beg;var<=end;var+=inc)
#define ForDec(var,end,beg) for(int var=end;var>=beg;--var)
#define ipArray(arr,size) ForInc(i,0,size-1) ip(arr[i]);
#define print(x) printf("%d\n",x)
#define printLL(x) printf("%lld\n",x)
#define ss(str) scanf("%s",str)
#define ii pair<int,int>
#define mp make_pair
#define pb push_back
#include<ctime>
template<typename T> T gcd(T a, T b) { return (b == 0) ? abs(a) : gcd(b, a % b); }
template<typename T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> inline T mod(T a, T b) { return (a % b + b) % b; }
template<typename T> inline T sqr(T x) { return x * x; }
typedef long long LL;
using namespace std;
/* Main Code starts here :) */
#define MAX 1000
int dz[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
string dir[4]={"E","N","W","S"};
int x,y;
//vector<bool> vis[MAX];
struct nd{
	ii pr;
	int lvl;
	string s;
};
/*void initializeVis(){
	ForInc(i,0,MAX-8){
		ForInc(j,0,MAX-8)vis[i].pb(false);
	}
}
void clearVis(int x, int y){
	ForInc(i,0,x){
		ForInc(j,0,y)vis[i][j]=false;
	}
}*/
int main(){
	
	//initializeVis();
	int t;ip(t);
	ForInc(cs,1,t){
		ip(x);ip(y);
		//clearVis(x,y);
		queue< nd > Q;
		map < ii,bool > M;
		nd temp,ext;temp.s="";temp.lvl=0;temp.pr.first=0;temp.pr.second=0;
		Q.push(temp);M.insert(mp(mp(0,0),true));//vis[0][0]=true;
		while(!Q.empty()){
			ext=Q.front();Q.pop();
			//printf("extracted: %d %d\n",ext.pr.first,ext.pr.second);
			if(ext.pr.first==x && ext.pr.second==y){
				printf("Case #%d: ",cs);cout<<ext.s;printf("\n");break;
			}
			ForInc(k,0,3){
				nd ins;
				ins.pr.first=ext.pr.first+dz[k][0]*(ext.lvl+1);
				ins.pr.second=ext.pr.second+dz[k][1]*(ext.lvl+1);
				ins.lvl=ext.lvl+1;
				ins.s=ext.s+dir[k];
				//printf("%d %d\n",ins.pr.first,ins.pr.second);
				if(M.find(mp(ins.pr.first,ins.pr.second))==M.end())
				{Q.push(ins);M.insert(mp(mp(ins.pr.first,ins.pr.second),true));
				 //printf("inserted: %d %d\n",ins.pr.first,ins.pr.second);
				}
			}
		}
	}
return 0;
}

