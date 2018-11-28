#include<iostream>

using namespace std;

main(){
	
		long long int A=0,B=0,K=0;
		int T=0,t=0;
		long long a=0,b=0,ans=0;
		
		
		cin>>T;
		
		while(t<T){
			
			t++;
			
			cin>>A;
			cin>>B;
			cin>>K;
			ans=A+B-1;
			cout<<"Case #"<<t<<": ";
			
			for(a=1;a<A;a++){
				
				for(b=1;b<B;b++){
					
					if((a&b)<K){
						ans++;
					}
					
				}
				
			}
			
			cout<<ans<<"\n";
			
		}
		
		
		
	
	
	
	
	return 0;
}
