#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
typedef long long ll;

char b[10008];
int a[10008],s[10008],com[5][5]={ {0,0,0,0,0}, {0,1,2,3,4}, {0,2,-1,4,-3}, {0,3,-4,-1,2}, {0,4,3,-2,-1} };

int main(){
	ll t,n,x,z,i,j;
	
	cin>>t;
	for(z=1;z<=t;z++){
		cin>>n>>x;
		cin>>b;
		
		int p=0,N=n*x;
		for(j=0;j<x;j++){
			for(i=0;i<n;i++){
				if(b[i]=='1')		a[p++]=1;
				else if(b[i]=='i')	a[p++]=2;
				else if(b[i]=='j')	a[p++]=3;
				else if(b[i]=='k')	a[p++]=4;
			}
		}
		
		int q,mul;
		s[0]=a[0];
		for(i=1;i<N;i++){
			p=a[i];
			q=s[i-1];
			
			mul=1;
			if(p<0){
				mul=-mul;
				p=-p;
			}
			if(q<0){
				mul=-mul;
				q=-q;
			}
			s[i]=mul*com[q][p];
		}
		
		int ans=0;
		if(s[N-1]==-1){
			for(i=0;i<N;i++){
				if(s[i]==2){
					for(j=i+1;j<N;j++){
						if(s[j]==4){
							ans=1;
							break;
						}
					}
					break;
				}
			}
		}
		if(ans==1)
			cout<<"Case #"<<z<<": YES"<<endl;
		else
			cout<<"Case #"<<z<<": NO"<<endl;
	}
	return 0;
}
