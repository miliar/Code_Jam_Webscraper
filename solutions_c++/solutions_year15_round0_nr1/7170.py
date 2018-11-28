#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
	int t,smax,res,sum;
	string s;
	cin>>t;
	for(int j=0;j<t;j++){
		res=0;
		sum=0;
		cin>>smax;
		cin>>s;
		int a[smax+1];
		for(int i=0;i<smax+1;i++){
			a[i]=(int)s[i]-48;
		}
		for(int i=1;i<smax+1;i++){
			sum+=a[i-1];
			if(sum<i){
				res+=i-sum;
				sum+=i-sum;
			}
		}
		cout<<"Case #"<<j+1<<": "<<res<<endl;
	}
}