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

int main() {
	ios::sync_with_stdio(false);
	lli t,tc=1;
	cin>>t;
	while(t--){
		lli n,ans,x,ct=0;
		cin>>n;
		lli arr[10];
		for(lli i=0;i<10;i++){
			arr[i]=0;
		}
		if(n==0){
			cout<<"Case #"<<tc<<": INSOMNIA\n";
			tc++;
			continue;
		}
		for(lli i=1;;i++){
			x=i*n;
			while(x){
				if(arr[x%10]==0){
					arr[x%10]++;
					ct++;
				}
				x=x/10;
			}
			if(ct==10){
				ans=i*n;
				break;
			}
		}
		cout<<"Case #"<<tc<<": "<<ans<<"\n";
		tc++;
	}
	return 0;
}