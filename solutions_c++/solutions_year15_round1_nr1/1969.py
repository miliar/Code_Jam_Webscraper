#include<iostream>
using namespace std;
int main(){
long int *ar,t,i1;
long long int min1,min2,mdiff;
int n,i;
cin>>t;
for(i1=1;i1<=t;i1++){
	cin>>n;
	min1=0;
	min2=0;
	mdiff=0;
	ar = new long int[n];
	for(i=0;i<n;i++){
	cin>>ar[i];
	}
	for(i=0;i<n-1;i++){
		if(ar[i]>ar[i+1]){
			min1+=ar[i]-ar[i+1];
			if((ar[i]-ar[i+1]) > mdiff){
				mdiff = ar[i]-ar[i+1];
			
			}
			
		}
	
	}
	for(i=0;i<n-1;i++){
		if(ar[i]<mdiff){
			min2+=ar[i];
		
		}
		else
			min2+=mdiff;
	
	}
	
	cout<<"Case #"<<i1<<": "<<min1<<" "<<min2<<endl;
}

}
