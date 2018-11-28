#include<iostream>

using namespace std;


int main(){
	
	int T=0,t=0,B,J=0;
	double Nb[1000],Kb[1000],temp,N[1000],K[1000];
	int i=0,j=0,Ns=0,Ks=0,k=0,l=0;
	bool found,loop=true;
	
	cin>>T;
	
	while(t<T){
		t++;
		cin>>B;
		
		for(i=0;i<B;i++)
			cin>>Nb[i];
			
			for(i=0;i<B;i++){
				for(j=1;j<B;j++){
					
					if(Nb[j-1]>Nb[j]){
						
						temp=Nb[j-1];
						Nb[j-1]=Nb[j];
						Nb[j]=temp;
					}
				}
			}
			
			for(i=0;i<B;i++){
			N[i]=Nb[i];
			//cout<<Nb[i]<<"->";
			}
			//cout<<"\n";
			
		
		for(i=0;i<B;i++)
			cin>>Kb[i];
		
			for(i=0;i<B;i++){
				for(j=1;j<B;j++){
					
					if(Kb[j-1]>Kb[j]){
						
						temp=Kb[j-1];
						Kb[j-1]=Kb[j];
						Kb[j]=temp;
					}
				}
			}
			
			
			for(i=0;i<B;i++){
			K[i]=Kb[i];
			//cout<<Kb[i]<<"->";
			}
			////finish inputs
			
			cout<<"Case #"<<t<<": ";
			
			//Decietful WAR
			loop=true;
			i=0;
			j=B-1;
			k=0;
			l=B-1;
			Ns=0;
			Ks=0;
			while(loop){
				
				if(i==j&&k==l){
					
					if(N[j]>K[l])
					Ns++;
					
					loop=false;
					
				}
				
				else if(N[j]>K[l]){
					Ns++;
					j--;
					l--;
				}
				else if(N[j]<K[l]){
					Ks++;
					i++;
					l--;
					
				}
				
				
				
				
			}
			
				cout<<Ns<<" ";
			
			
			
			
			
			
			//WAR
			Ns=0;
			Ks=0;
			
			for(i=0;i<B;i++){
				found = false;
				for(j=0;j<B;j++){
					
					if(Nb[i]<Kb[j]){
						found =true;
						Ks++;
						Kb[j]=0.0;
						break;
					}
					
				}
				
				if(found==false){
					for(i=0;i<B;i++){
						if(Kb[i]!=0.0){
							Kb[i]=0.0;
							Ns++;
						}
					}
				}
				
				
				
			}
			
			cout<<Ns<<"\n";
			
			
	}
	
	
	
	return 0;
}