#include <iostream>
#include <string>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <list>
using namespace std;

#define ll long long
#define ull unsigned long long
#define INF 1e9

ll gcd(ll a, ll b){
	if(b>a) return gcd(b,a);
	if( b==0)
		return a;
	else
		return gcd(b,a%b);
}

int main(){
	ios_base::sync_with_stdio(0);
	long t,p,q,result;
	char c;
	ll pows[40];
	pows[0] = 1;
	for(int i=1;i<41;i++){
		pows[i] = 2* pows[i-1];
	}	
	cin>>t;
	for(int a=1;a<=t;a++){
		bool flag = false;
		cin>>p>>c>>q;
		ll g = gcd(p,q);
		p = p/g;
		q = q/g;
		if(p<=q){
			for(int i=0;i<41;i++){
				if(pows[i]==q){
					result = i;
					flag = true;
					break;
				}
			}
		}
		if(flag){
			result=0;
			if(p==q) {
			    cout<<"Case #"<<a<<": 1"<<endl;
			}
			while(p<q) {
			    p*=2;
			    result++;
			}
			cout<<"Case #"<<a<<": "<<result<<endl;
		}else{
			cout<<"Case #"<<a<<": impossible"<<endl;
		}		
	}
	
	return 0;
}
