#include <iostream>
#include<cstdio>
using namespace std;
int cases,caseno=1,n;
int main() {
    freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
	cin>>cases;
	while(cases--){
		cin>>n;
		cout<<"Case #"<<caseno++<<": ";
		if(n==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		long long ans=0,t;
		int res=0,b=1,x;
		while(res!=(1<<10)-1){
			t=b*n;
			ans=t;
			while(t){
				x=t%10;
				res|=(1<<x);
				t/=10;
			}
			b++;
		}
		cout<<ans<<endl;
	}
	return 0;
}
