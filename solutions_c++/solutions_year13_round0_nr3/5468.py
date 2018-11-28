#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
using namespace std;
int main(){
	//freopen("test","r",stdin);
	//freopen("out","w",stdout);
	int t,a,b,index=1;
	int aa[]={1,4,9,121,484};
	cin>>t;
	while(t--){
		cin>>a>>b;
		int ans=0;
		for(int i=0;i<5;i++) if(aa[i]>=a && aa[i]<=b) ans++;
		cout<<"Case #"<<index<<": "<<ans<<endl;
		index++;
	}
	return 0;
}
