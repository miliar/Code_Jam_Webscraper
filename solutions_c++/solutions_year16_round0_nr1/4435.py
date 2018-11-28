#include<iostream>
#include<unistd.h>
using namespace std;
int main(){

	int t;
	cin>>t;
	int i=1;
	for(i=1;i<=t;i++){
		long int n;
		int arr[10]={0,0,0,0,0,0,0,0,0,0};
		int z=0;
		//cout<<arr[2]<<endl;
		cout<<"CASE #"<<i<<": ";
		cin>>n;
		//cout<<n;
		if(n==0){
			cout<<"INSOMNIA"<<endl;
		}
		else{ 
			long int j =1;
			
		
			while(z<10){
			     //cout<<"here";
			     
			     long int k=n*j;
			    // cout<<k<<endl;
			     while(k){
			     	//cout<<"\n"<<arr[k%10]<<"\n";
			     	if(arr[k%10]==0){
			     		//cout<<"\neverywhere\n";
			     		arr[k%10]=1;
			     		z++;
			     		//cout<<z<<endl;
			     	}
			     	k=k/10;
			     
			     }
			
			     j=j+1;
			    
			     //usleep(100000);
			
			
			}
			cout<<(j-1)*n<<endl;
		
		
		}
	
	}




}
