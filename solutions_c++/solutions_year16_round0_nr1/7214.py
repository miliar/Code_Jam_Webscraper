#include<bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
	freopen("code2.out","w",stdout);
	int t,n;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		if(n==0)
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else{
			bool mark[10];
			memset(mark,false,sizeof(mark[0])*10);
			int count=0;
			long long int j=1,k;
			while(count!=10){
				k=n*j;
				while(k>0){
					int x=k%10;
					if(mark[x]==false){
						mark[x]=true;
						count++;
						//cout<<"in ";
					}
					k/=10;
				}
				j++;
				
				//cout<<" out ";
			}
			cout<<"Case #"<<i<<": "<<1ll*(n)*(j-1)<<endl;
		}
		
		
	}
	
}
