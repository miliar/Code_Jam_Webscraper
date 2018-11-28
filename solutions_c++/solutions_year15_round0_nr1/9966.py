#include<iostream>

using namespace std;


int ctoi(char a){
	
	if(a=='0'){
		return 0;
	}
	
	else if(a=='1'){
		return 1;
	}
	
	else if(a=='2'){
		return 2;
	}
	
	else if(a=='3'){
		return 3;
	}
	
	else if(a=='4'){
		return 4;
	}
	
	else if(a=='5'){
		return 5;
	}
	
	else if(a=='6'){
		return 6;
	}
	
	else if(a=='7'){
		return 7;
	}
	
	else if(a=='8'){
		return 8;
	}
	
	else if(a=='9'){
		return 9;
	}
	
}


int main(){
	
	long int T=0;
	long int Sm=0, F=0,temp,Ps=0,c=1;
	char a;
	
	cin>>T;
	
	while(T--){
		
		
		cin>>Sm;
		
		F=0; Ps=0;
		temp=0;
		
		for(int i =0;i<=Sm;i++){
			cin>>a;
			temp=ctoi(a);
			
			if(i==0 || temp==0){
				Ps+=temp;
			}
			
			else if(Ps>=i){
				Ps+=temp;
			}
			
			else if(Ps<i){
				F+=i-Ps;
				Ps += (F+temp);
				
			}
			
			//cout<<"Step: "<<"temp="<<temp<<" i="<<i<<" Ps="<<Ps<<" F="<<F<<"\n";
			
		}
	
	
	cout<<"Case #"<<c++<<": "<<F<<"\n";
		
	}	
		
		
			
	return 0;
}
