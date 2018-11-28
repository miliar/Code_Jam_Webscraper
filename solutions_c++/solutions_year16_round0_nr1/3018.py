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

int hash[10];

bool check(){
    for(int i=0;i<10;i++)
        if(!hash[i])
            return false;
    return true;
}

void mark(ll num){
    while(num){
        hash[num%10]=1;
        num/=10;
    }
}

int main() {
    freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
    ios::sync_with_stdio(0);
    int tc,i;
	ll ans,n;
    cin>>tc;
    for(int t=1;t<=tc;t++){
		cin>>n;
		if(n==0){
            cout<<"Case #"<<t<<": INSOMNIA\n";
            continue;
		}
		for(i=0;i<10;i++) hash[i]=0;
		ans = 0;
		for(i=1;i<=100000;i++){
            ans+=n;
            mark(ans);
            if(check())
                break;
		}
        cout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	return 0;
}
