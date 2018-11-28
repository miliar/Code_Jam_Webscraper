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

li b;
li n;
li m[101010];

li divup(li a, li b){
	li res=a/b;
	if(a%b>0)res++;
	return res;
}

bool check(li x){
	li total=0;
	rep(i,b){
		total+=(x/m[i])+1;
	}
	return total>=n;
}

li solve(){
	li l=-1,r=100000ll*1000000000ll+100000ll;

	while(l+1<r){
		li mi=(l+r)/2;
		if(check(mi)){
			r=mi;
		}
		else{
			l=mi;
		}
	}

	l+=10;
	while(check(l))l--;


	li total=0;
	rep(i,b){
		total+=(l/m[i])+1;
	}
	rep(i,b){
		if((l+1)%m[i]==0){
			total++;
			if(total>=n)return i+1;
		}
	}
	return -1;
}

int main(int argc, char *argv[]){
	li t;
	cin>>t;
	rep(case_num,t){
		cin>>b>>n;
		rep(i,b)cin>>m[i];

		cout<<"Case #"<<case_num+1<<": "<<solve()<<endl;
	}
	return 0;
}