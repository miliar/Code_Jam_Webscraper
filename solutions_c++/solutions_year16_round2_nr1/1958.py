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

string digit[10]={
"ZERO",
"ONE",
"TWO",
"THREE",
"FOUR",
"FIVE",
"SIX",
"SEVEN",
"EIGHT",
"NINE"
};

li order[10]={
	0,2,4,6,8,1,3,5,7,9
};

map<char,li> digit_map[10];

void init_digit_map(){
	rep(i,10){
		rep(j,sz(digit[i])){
			digit_map[i][digit[i][j]]++;
		}
	}
}

void decrease(li num, map<char,li> &m, map<li,li> &res){
	while(true){

		repp(c,'A','A'+26){
			//p3(m[c],digit_map[num][c],num);
		}
		repp(c,'A','A'+26){
			if(m[c]<digit_map[num][c])return;
		}
		res[num]++;
		repp(c,'A','A'+26){
			m[c]-=digit_map[num][c];
		}
	}
}

void solve(li case_num){
	map<char,li> m;
	string s;
	cin>>s;
	rep(i,sz(s)){
		m[s[i]]++;
	}
	map<li,li> res;
	rep(i,10){
		decrease(order[i], m, res);
	}

	cout<<"Case #"<<case_num+1<<": ";
	rep(i,10){
		rep(j,res[i])cout<<i;
	}
	cout<<endl;
}

int main(int argc, char *argv[]){
	init_digit_map();
	rep(num,10){
		repp(c,'A','A'+26){
			//p3(c,digit_map[num][c],num);
		}
	}
	li t;
	cin>>t;
	rep(case_num,t){
		solve(case_num);
	}
	return 0;
}
