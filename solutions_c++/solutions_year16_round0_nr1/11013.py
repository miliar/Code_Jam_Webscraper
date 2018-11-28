#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin>>t;
	ll n[t];
	for(int i=0;i<t;i++) {
		int A[10]={0},c,j=1;
		ll n1,n2,k1;
		cin>>n[i];
		if(n[i]==0) cout<<"Case #"<<i+1<<": INSOMNIA\n";
		else if(n[i]==1) cout<<"Case #"<<i+1<<": 10\n";
		else if(n[i]>1) {
			c=0;
			while(c<10) {
				c=0;
				n1=n2=j*n[i];
				//cout<<"n1="<<n1<<" n2="<<n2<<endl;
				while(n1) {
					k1=n1%10;
					//cout<<"\nk1="<<k1<<endl;
					A[k1]++;
					n1/=10;
				}
				j++;
				for(int k=0;k<10;k++) {
				//cout<<k<<" "<<A[k]<<"\n";
				if(A[k]>=1)	c++;
				
				
			}	
				if(c==10) break;	
			}
			cout<<"Case #"<<i+1<<": "<<n2<<"\n";
		
		}
	}
	
	
	return 0;
}
