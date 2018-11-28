#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <cstring>
#include <map>
#include <vector>
#define FOR(i,n)for(ll i=0;i<n;i++)
#define FORR(i,k,n)for(ll i=k;i<n;i++)

using namespace std;
typedef unsigned long long int ll;

vector<string>s;
int main() {
	ll t,tt,r,c,w,sum,pos,L,R;cin>>t;tt=t;
	while(t--){
		cout<<"Case #"<<tt-t<<": ";
		cin>>r>>c>>w;sum=0;
		if(c==w){cout<<w<<"\n";continue;}
		if(w==1){cout<<c<<"\n";continue;}
		ll i,inc=w-1;
		for(i=0;i<c;i+=w)if(i!=0)sum++;
		
		pos = i;
		if(pos == c-1){cout<<sum+w-1<<"\n";}
		else cout<<sum+w<<"\n";
	}
	return 0;
}
