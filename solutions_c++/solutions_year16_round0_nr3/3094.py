//Naman Agarwal
//IIT Mandi
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <string>

using namespace std;

#define lli long long int
int printed=0;
lli isc(lli n){
    for(lli i=2;i*i<=n;i++){
        if(n%i==0)
            return i;
    }
    return 0;
}
lli bb(string s,int base){
    int n=s.length();
    lli ans=0;
    for(lli i=0;i<n;i++){
        ans=ans+(s[i]-48)*pow(base,n-i-1);
    }
    return ans;
}
void go(string s,int n,int j,int done){
    if(printed<j){
    if(done==0){
        go("1",n,j,1);
    }
    if(done==n-1){
        go(s+"1",n,j,done+1);
    }
    if(done>0&&done<n-1){
    go(s+"1",n,j,done+1);
    go(s+"0",n,j,done+1);
    }
    if(done==n){
        if(isc(bb(s,2))&&isc(bb(s,3))&&isc(bb(s,4))&&isc(bb(s,5))&&isc(bb(s,6))&&isc(bb(s,7))&&isc(bb(s,8))&&isc(bb(s,9))&&isc(bb(s,10))){
            //cout<<s<<" "<<bb(s,2)<<" "<<bb(s,3)<<" "<<bb(s,4)<<" "<<bb(s,5)<<" "<<bb(s,6)<<" "<<bb(s,7)<<" "<<bb(s,8)<<" "<<bb(s,9)<<" "<<bb(s,10)<<"\n";
            cout<<s<<" "<<isc(bb(s,2))<<" "<<isc(bb(s,3))<<" "<<isc(bb(s,4))<<" "<<isc(bb(s,5))<<" "<<isc(bb(s,6))<<" "<<isc(bb(s,7))<<" "<<isc(bb(s,8))<<" "<<isc(bb(s,9))<<" "<<isc(bb(s,10))<<"\n";
            printed++;
        }
    }
    }
}
int main() {
	ios::sync_with_stdio(false);
	int t,tc=1;
	cin>>t;
	while(t--){
		lli n,j;
		cin>>n>>j;
		cout<<"Case #"<<tc<<":\n";
		go("",n,j,0);
		tc++;
	}
	return 0;
}
