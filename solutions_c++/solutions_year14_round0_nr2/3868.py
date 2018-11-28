#include<iostream>
#include<stdio.h>
using namespace std;

main(){
	
	int T=0,t=0;
	
	double C=0,F=0,X=0,R=2.0;
	double total=0, time=0,farm=0,finish1=0,finish2=0;
	cin>>T;
	bool loop = true;
	while(t<T){
		
		t++;
		total=0;
		time=0;
		farm=0;
		finish1=0;
		finish2=0;
		R=2.0;
		loop =true;
		cin>>C;
		cin>>F;
		cin>>X;
		cout<<"Case #"<<t<<": ";
		total=X/R;
		farm=C/R;
		
		if(total<farm){
			printf("%7.7f\n",total);
		}
		
		
		
		
		else{
			
			
			time=farm;
		    
			
			R+=F;
			finish1 = time + X/R;
			
			if(total<finish1){
				printf("%7.7f\n",total);
				loop = false;
			}
			
			while(loop){
				
				
				
				farm = C/R;
				
				R+=F;
				finish2 = time + farm + X/R;
				
				if(finish2>finish1){
					
				printf("%7.7f\n",finish1);
				
				break;
			}
				
				time = time + farm;
				finish1=finish2;
				
			
			}
			
			
			
		}
		
	}

	
	return 0;
}