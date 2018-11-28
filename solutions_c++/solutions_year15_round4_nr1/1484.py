#include <bits/stdc++.h>
#define _USE_MATH_DEFINES
using namespace std;
 
 
#define li			long long int
#define rep(i,to)	for(li i=0;i<((li)(to));i++)
#define repp(i,start,to)	for(li i=(li)(start);i<((li)(to));i++)
#define pb			push_back
#define sz(v)		((li)(v).size())
#define bgn(v)		((v).begin())
#define eend(v)		((v).end())
#define allof(v)	(v).begin(), (v).end()
#define dodp(v,n)		memset(v,(li)n,sizeof(v))
#define bit(n)		(1ll<<(li)(n))
#define mp(a,b)		make_pair(a,b)
#define rin	rep(i,n)
#define rjm	rep(j,m)
#define VV			vector


#define DBGP 1


#define idp if(DBGP)
#define F first
#define S second
#define p2(a,b)		idp cout<<a<<"\t"<<b<<endl
#define p3(a,b,c)		idp cout<<a<<"\t"<<b<<"\t"<<c<<endl
#define p4(a,b,c,d)		idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<endl
#define p5(a,b,c,d,e)		idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<endl
#define p6(a,b,c,d,e,f)		idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<endl
#define p7(a,b,c,d,e,f,g)		idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<endl
#define p8(a,b,c,d,e,f,g,h)		idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<"\t"<<h<<endl
#define p9(a,b,c,d,e,f,g,h,i)		idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<"\t"<<h<<"\t"<<i<<endl
#define p10(a,b,c,d,e,f,g,h,i,j)		idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<"\t"<<h<<"\t"<<i<<"\t"<<j<<endl
#define foreach(it,v)	for(__typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define p2p(x)		idp p2((x).F, (x).S)
#define dump(x,n)	idp{rep(i,n){cout<<x[i]<<" ";}puts("");}
#define dump2(x,n)	idp{rep(i,n){cout<<"["<<x[i].F<<" , "<<x[i].S<<"] ";}puts("");}
#define dumpi(x)	idp{foreach(it, x){cout<<(*it)<<" ";}puts("");}
#define dumpi2(x)	idp{foreach(it, x){cout<<"["<<(it)->F<<" , "<<(it)->S<<"] ";}puts("");}



#define EPS 1e-10
#define ETOL 1e-8
#define MOD 1000000007

#define PRIME_MAX 1000001

typedef pair<li, li> PI;

li r,c;
string board[110];

bool flg[110][110][4];

char dir[4]={'^','v','>','<'};

li solve(){
	li res=0;
	bool flg_t[110]={false};
	rep(i,r)rep(j,c)rep(k,4)flg[i][j][k]=false;

	// v : ue kara shita he
	rep(i,r){
		rep(j,c){
			flg[i][j][0]=flg_t[j];
			if(!flg_t[j] && board[i][j]!='.'){
				if(board[i][j]=='^')res++;
				flg_t[j]=true;
			}
		}
	}

	rep(i,110)flg_t[i]=false;


	// ^ : shita kara ue he
	for(li i=r-1; i>=0; i--){
		rep(j,c){
			flg[i][j][1]=flg_t[j];
			if(!flg_t[j] && board[i][j]!='.'){
				if(board[i][j]=='v')res++;
				flg_t[j]=true;
			}
		}
	}

	rep(i,110)flg_t[i]=false;



	// > : hidri kara migi he
	rep(j,c){
		rep(i,r){
			flg[i][j][2]=flg_t[i];
			if(!flg_t[i] && board[i][j]!='.'){
				if(board[i][j]=='<')res++;
				flg_t[i]=true;
			}
		}
	}

	rep(i,110)flg_t[i]=false;

	// < : migi kara hidari he
	for(int j= c-1; j>=0; j--){
		rep(i,r){
			flg[i][j][3]=flg_t[i];
			if(!flg_t[i] && board[i][j]!='.'){
				if(board[i][j]=='>')res++;
				flg_t[i]=true;
			}
		}
	}

	rep(i,110)flg_t[i]=false;


	// dame check
	rep(i,r){
		rep(j,c){
			if(board[i][j]=='.')continue;
			bool dame=true;
			//p2(i,j);
			//rep(k,4){
			//	if(flg[i][j][k])cout<<"true  ";
			//	else cout<<"false ";
			//}puts("");
			rep(k,4){
				if(flg[i][j][k]){
					dame=false;
					break;
				}
			}
			if(dame)return -1;
		}
	}

	return res;
}

int main(int argc, char *argv[]){
	li t;
	cin>>t;
	rep(case_num,t){
		cin>>r>>c;
		rep(i,r)cin>>board[i];

		li res=solve();

		cout<<"Case #"<<case_num+1<<": ";
		if(res>=0)cout<<res<<endl;
		else puts("IMPOSSIBLE");
	}
	return 0;
}