#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <fstream>
#define mod 1000000007
#define size 1000007
#define ll long long
#define INF LLONG_MAX
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;

int main() {
    freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
    ios::sync_with_stdio(0);
    int tc,i,C,S,K;
	ll ans;
    cin>>tc;
    for(int t=1;t<=tc;t++){
        cin>>K>>C>>S;
		cout<<"Case #"<<t<<": ";
		for(i=1;i<=S;i++)
            cout<<i<<" ";
		cout<<"\n";
	}
	return 0;
}
