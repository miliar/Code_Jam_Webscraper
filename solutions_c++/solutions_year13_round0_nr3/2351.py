#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
#include <queue>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;

typedef long long ll;
#define REP(i,k) for(int (i)=0;(i)<(k);(i)++)
#define INF ~(1<<31)
#define CLR(a) memset((a),0,sizeof((a)))
#define EPS 1e-9
#define DBG 1
#define D(s,v) if(DBG) cout<<(s)<<": "<<(v)<<endl;
#define DVEC(s,v) if(DBG) {cout<<(s)<<": "; for(int i=0;i<(v).size();i++) cout<<(v)[i]<<" "; cout<<endl;}
#define DARR(s,v,n) if(DBG) {cout<<(s)<<": "; for(int i=0;i<n;i++) cout<<(v)[i]<<" "; cout<<endl;}

bool chk(ll x){
	if(x==0) return 1;
	
	ll t = x;
	ll z = 0;
	while(t>0){
		z*=10;
		z+=(t%10);
		t/=10;
	}
	
	return (z==x);
}

int main(){
ios_base::sync_with_stdio(0);
int T;
cin>>T;

for(int cs=1;cs<=T;cs++){
	ll A,B;
	cin>>A>>B;
	
	ll res = 0;
	
	/*for(ll i=1;i<=10000005;i++){
		ll x = i*i;
		if(x>B) break;
		if(x>=A){
			if(chk(i) && chk(x)){			
				res++;
				cout<<x<<"ll,";
			}
		}
	}*/
	
	ll z[] = {1ll,4ll,9ll,121ll,484ll,10201ll,12321ll,14641ll,40804ll,44944ll,1002001ll,1234321ll,4008004ll,100020001ll,102030201ll,104060401ll,121242121ll,123454321ll,125686521ll,400080004ll,404090404ll,10000200001ll,10221412201ll,12102420121ll,12345654321ll,40000800004ll,1000002000001ll,1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,1024348434201ll,1210024200121ll,1212225222121ll,1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll};
	
	for(int i=0;i<39;i++){
		if(A<=z[i] && z[i]<=B) res++;
	}
		
	cout<<"Case #"<<cs<<": ";
	cout<<res<<endl;
}

}