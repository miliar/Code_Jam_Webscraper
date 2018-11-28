#include <bits/stdc++.h>
#define ll long long 
#define pb push_back
#define pii pair<int,int>
#define pll pair<ll int,ll int>
#define pdd pair<double,double> 
#define p push 
#define maxn 100001
#define modi 1000000007
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		string a;
		cin>>a;
		int counter=0;
		for(int j=a.length()-1;j>=1;j--){
			if(a[j]!=a[j-1]){
				if( (a[j]=='-' && counter%2==0) || (a[j]=='+' && counter%2==1) ){
					counter++;				  
				}
			}
		}
		if((a[0]=='-' && counter%2==0) ||(a[0]=='+' && counter%2==1))
			counter++;
		cout<<"Case #"<<i<<": "<<counter<<"\n";
	}
}
