#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int bool_and(int a, int b){
	if(a ==0 || b == 0)return 0;
	if(a%2 == 1 && b%2 == 1)return 1 + 2*bool_and(a/2,b/2);
	return 2*bool_and(a/2,b/2);
}
int main(){
	int t;
	int a,b,k;
	cin>>t;
	int ans;
	for(int i=0;i<t;i++){
		cin>>a;
		cin>>b;
		cin>>k;
		ans=0;
		for(int j=0;j<a;j++){
			for(int m=0;m<b;m++){
				if(min(j,m) < k)ans++;
				else{
					//cout<<"j "<<j<<" m "<<m<<" and "<< bool_and(j,m)<<"\n";
					if(bool_and(j,m) < k)ans++;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<"\n";
	}
}
