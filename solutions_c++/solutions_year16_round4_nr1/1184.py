#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;

#define pb push_back
#define pi pair<ll,ll>
#define pii pair<pi,ll>
#define f first
#define s second
#define ll long long
#define mod 1000000007
#define rep(i,n) for(ll i=0;i<n;i++)
string func(char r,int n){
	if(n==0){
		string s="";
		s+=r;
		return s;
	}
	if(r=='R'){
		string A=func('R',n-1);
		string B=func('S',n-1);
		if(A>B){
			return B+A;
		}
		return A+B;

	}
	else if(r=='P'){
		string A=func('P',n-1);
		string B=func('R',n-1);
		if(A>B){
			return B+A;
		}
		return A+B;
		
	}
	else{
		string A=func('S',n-1);
		string B=func('P',n-1);
		if(A>B){
			return B+A;
		}
		return A+B;
		
	}
}
int n,R,P,S;
bool valid(string &A){
	int r=0;
	int p=0;
	int s=0;
	rep(i,A.size()){
		r+=(A[i]=='R');
		p+=(A[i]=='P');
		s+=(A[i]=='S');
	}
	return (r==R and p==P and s==S);
}
int main(){
	
	freopen("A-large.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	rep(tt,t) {
		cin >> n >> R>> P >> S;
		string ans="";
		string P1=func('R',n);
		string P2=func('S',n);
		string P3=func('P',n);
		if(valid(P1)){
			if(ans.size()==0 or ans >P1) ans=P1;
		}
		if(valid(P2)){
			if(ans.size()==0 or ans >P2) ans=P2;
		}
		if(valid(P3)){
			if(ans.size()==0 or ans >P3) ans=P3;
		}
		if(ans.size()==0) ans="IMPOSSIBLE";
		cout<<"Case #"<<tt+1<<": "<<ans<<"\n";
	}

}