#include<bits/stdc++.h>

using namespace std;

int main(){
	
	int t,x,r,c;
	
	cin>>t;
	
	for(int j=1;j<=t;j++){
		
			cin>>x>>r>>c;
			
			if(x==1)
				cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
			
			if(x==2){
			
				if( r*c==1 || r*c==3 || r*c==9)
					cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
				else
					cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
			}
			
			if(x==3){
				
				if( (r<=2 && c<=2) || r*c==3 || r*c ==4 || r*c==8 || r*c==16)  
					cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
				else
					cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
			}
				
			if(x==4){
				
				if((r<=3 && c<=3) || r*c==4 || r*c==8)
					cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
				else
					cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
			}
			
		}
	
	return 0;
}
		
		
	
	
