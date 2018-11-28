#include<iostream>
using namespace std;

int main(){
	int T,cur[4],prev[4],n=0,i,j,k,x,count;
	cin>>T;
	for(i=0;i<T;i++){
		count=0;
		cin>>n;
		for(j=0;j<4;j++){
			if(j==n-1)
				for(k=0;k<4;k++)
					cin>>prev[k];
			else
				for(k=0;k<4;k++)
					cin>>x;
		}
					
		cin>>n;
		for(j=0;j<4;j++){
			if(j==n-1)
				for(k=0;k<4;k++)
					cin>>cur[k];
			else
				for(k=0;k<4;k++)
					cin>>x;
			
		}
				
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				if(cur[j] == prev[k]){
					x=cur[j];
					count++;
				}
		
		cout<<"Case #"<<i+1<<": ";
		if(count==1)
			cout<<x<<"\n";
		else if(count==0)
			cout<<"Volunteer cheated!\n";
		else
			cout<<"Bad magician!\n";
	}
	
	
}
