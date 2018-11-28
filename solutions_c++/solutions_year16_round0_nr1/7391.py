#include<iostream>
using namespace std;

int main(){
	
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long n;
		cin>>n;
		//for(n=0;n<=1000000;n++){
		
		long k=n,x;
		bool p[10] = {};
		int ans=10;
		
		if(n!=0){
			while(1){
				x=k;
				while(x){
					if(!p[x%10]){
						ans--;
						if(ans==0){
							break;
						}
						p[x%10]=1;
					}
					x/=10;
				}
				if(ans==0){
					break;
				}
				k+=n;
			}
			cout<<"Case #"<<i<<": "<<k<<"\n";
		}
		else{
			cout<<"Case #"<<i<<": INSOMNIA\n";
		}

	}
//	}//
}

