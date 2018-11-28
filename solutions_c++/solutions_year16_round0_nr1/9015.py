#include<bits/stdc++.h>
 
using namespace std;
 
int main(){
 
 	//std::ios_base::sync_with_stdio(false);cin.tie(false);
	long long t,n,i,j,k,l,x=0;
	cin>>t;
	for(x=1;x<=t;x++){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<x<<": INSOMNIA\n";
		}
		else{
			int left = 10;
			map<int, int> digit;
			i=2;
			k= n;
			l=k;
			while(left){
				if(digit[k%10]==0){
					digit[k%10]=1;
					left--;
				}
				k/=10;
				if(k==0&&left){
					k = n*i;
					i++;
					l=k;
				}
			}
			cout<<"Case #"<<x<<": "<<l<<"\n";
			
		}
	}
 
	return 0;
}
