#include <bits/stdc++.h>

using namespace std;
long long ans[1000010];
int main(){
	#define int long long
	clock_t ti=clock();
	int n;
	for(n=1;n<=1000000;n++){
//	while(cin>>n){
		int finded=0,mul=1;
		while(finded!=1023){
			int res=mul*n;
			while(res>0){
				finded|=(1<<(res%10));
				res/=10;
			}
			mul++;
		}
		ans[n]=(mul-1)*n;
//		cout<<n<<": "<<mul<<endl;
	}
	int tc,i=0;
	cin>>tc;
//	cout<<"process_time: "<<(clock()-ti)/CLOCKS_PER_SEC<<endl;
	while(tc-->0){
		int q;
		i++;
		cin>>q;
		cout<<"Case #"<<i<<": ";
		if(q!=0)cout<<ans[q]<<endl;
		else cout<<"INSOMNIA"<<endl;
	}
	return 0;
} 
