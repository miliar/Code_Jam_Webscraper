#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

#define ll long long
#define pi pair<int,int>
#define X first 
#define Y second
#define pb push_back
#define ab(x) ((x)<0?(-(x)):(x))
#define xx(x) ((x)*(x))
#define D 1000000007
#define Max (1<<30)
#define LLMAX (1ll<<60)
#define mp make_pair
#define MM 1000000000000000000ll
#define pss pair<string,string>
#define psi pair<string,int>
#define NN 3
#define vi vector<int>


string P,Q;
vi A,B;
ll tot=0;


vi MUL(vi x,vi y){
	
	reverse(x.begin(),x.end());
	reverse(y.begin(),y.end());

	vi r(150,0);
	int flag=0;

	int n=x.size();
	int m=y.size();

	for(int i=0;i<n;i++){
		for(int k=0;k<m;k++){
			int v=x[i]*y[k];
			int now=i+k;

			r[now]+=v;
		}
	}

	for(int i=0;i<r.size()-1;i++){
		r[i+1]+=r[i]/10;
		r[i]%=10;
	}
	while(r.back()==0)r.pop_back();
	reverse(r.begin(),r.end());
	return r;

}

bool can( vi  x){
	int L=x.size();
	if(A.size() < L  && L < B.size())return 1;
	bool s = x>=A;
	bool e = x<=B;

	if(A.size()==L && B.size()==L)return s && e;
	if(A.size()==L)return s;
	if(B.size()==L)return e;
	return 0;

}
bool can(int n,bool ck,ll T){
	vi now;

	if(ck){
		if(tot==T){
			now.pb(2);
			for(int i=1;i<=n*2-1;i++)now.pb(0);
			now.pb(2);

			now[now.size()/2]=1;

			return can(MUL(now,now));

		}else if(tot==T+1){
			now.pb(2);
			for(int i=1;i<=n*2-1;i++)now.pb(0);
			now.pb(2);

			return can(MUL(now,now));
		}

	}else{
		if(tot==T){
			now.pb(2);
			for(int i=1;i<=n*2;i++)now.pb(0);
			now.pb(2);

			return can(MUL(now,now));
		}
	}

	T--;
	now.pb(1);
	for(int i=n-1;i>=1;i--){
		ll val=(1ll<<i);
		
		if(ck){
			if(i)val+=(1ll<<(i-1));
			else val++;
		}
		if(val<=T){
			T-=val;
			now.pb(1);
		}else{
			now.pb(0);
		}
	}
	now.pb(T);
	int k=now.size();
	if(ck)for(int i=k-2;i>=0;i--)now.pb(now[i]);
	else for(int i=k-1;i>=0;i--)now.pb(now[i]);

	return can(MUL(now,now));
}

ll calcS(int n,bool ck){
	tot=0;
	ll S=2;
	ll E=(1ll<<n) + 1;
	if(ck)E+=(1ll<<(n-1)) + 1;
	tot=E;

	ll r=0;
	while(S<=E){
		ll M=(S+E)/2;

		if(can(n,ck,M))r=M,E=M-1;
		else S=M+1;
	}

	return tot-r+1;


}

ll calcE(int n,bool ck){
	tot=0;
	ll S=1;
	ll E=(1ll<<n) + 1;
	if(ck)E+=(1ll<<(n-1)) + 1;
	tot=E;

	ll r=0;
	while(S<=E){
		ll M=(S+E)/2;

		if(can(n,ck,M))r=M,S=M+1;
		else E=M-1;
	}

	return r;
}
int main(){
	
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	
	int t;
	cin>>t;
	vi t1,t2,t3,t4,t5;
	int CC=0;
	
	t1.pb(1);
	t2.pb(4);
	t3.pb(9);

	t4.pb(1);
	t4.pb(2);
	t4.pb(1);
	
	t5.pb(4);
	t5.pb(8);
	t5.pb(4);
	while(t--){
		CC++;
		cin>>P>>Q;

		A.clear();
		B.clear();

		for(int i=0;i<P.size();i++)A.pb(P[i]-'0');
		for(int i=0;i<Q.size();i++)B.pb(Q[i]-'0');
		ll rst=0;

		
		if(can(t1))rst++;
		if(can(t2))rst++;
		if(can(t3))rst++;
		if(can(t4))rst++;
		if(can(t5))rst++;

		for(int Len=3;Len<=50;Len++){
			
			bool S=0;
			bool E=0;
			vi F,L;

			F.pb(1);
			for(int i=2;i<=Len-1;i++)F.pb(0);
			F.pb(1);

			L.pb(2);
			for(int i=2;i<=Len-1;i++)L.pb(0);
			L.pb(2);

			if(Len%2)L[Len/2]=1;

			S=can(MUL(F,F));
			E=can(MUL(L,L));

			int n=(Len-1)/2;
			if(S && E){

				rst+=(1ll<<n);
				rst++;

				if(Len%2)rst+=(1ll<<(n-1)) + 1;
				

			}else if(S){
				rst+=calcE(n,Len%2);

			}else if(E){
				rst+=calcS(n,Len%2);
			}
		}

		printf("Case #%d: ",CC);
		cout<<rst<<endl;
	}
	
	/*
	for(ll i=1;i<=100000000;i++){
		if(pal(i) && pal(xx(i)) ){
			cout<<i<<" "<<xx(i)<<endl;
		}
	}*/
}