#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
	
int a[1000];
int main(){
	int TT;
	cin>>TT;


	int n;
	int x;
	int s[11000];
	for(int T=1;T<=TT;++T){
		cin>>n>>x;

		for(int i=0;i<=x;++i){
			a[i]=0;
		}
		for(int i=0;i<n;++i){
			cin>>s[i];
			a[s[i]]++;
		}
		int count=0;
		for(int i=0;i<=x;++i){
			while(a[i]>0){
				--a[i];
				++count;
				for(int j=x-i;j>=0;--j){
					if(a[j]>0){
						--a[j];
						break;
					}
				}
			}
		}
		int ans=count;
		cout<<"Case #"<<T<<": "<<ans<<"\n";



	}
	return 0;
}
