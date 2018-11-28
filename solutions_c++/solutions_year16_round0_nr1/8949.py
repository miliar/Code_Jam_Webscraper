#include<iostream>
using namespace std;

int main(){
	long long int t,n,q,d,i,j,k;
	
	
	cin>>t;
	
	for(k=0;k<t;k++){
		cin>>n;
		int prime=0;
		long long int arr[]={0,1,2,3,4,5,6,7,8,9};
		if(n==0){
			
				cout<<"Case #"<<k+1<<": INSOMNIA"<<endl;
				continue;
		}
		i=1;
		while(1){
			q=n*i;
			
			while(q!=0){
				d=q%10;
				q=q/10;
				
				for(j=0;j<10;j++){
					if(arr[j]==d)
					{
						arr[j]=-1;
						break;
					}
				}
				
			}
			
			
			for(j=0;j<10;j++){
				if(arr[j]!=-1)
					break;
					
				if(j==9){
				cout<<"Case #"<<k+1<<": "<<n*i<<endl;
				prime=1;
				
		  		}
			
			}
			if(prime==1)
				break;
			i++;
		}
	}
}
