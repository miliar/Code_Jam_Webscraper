#include<bits/stdc++.h>
using namespace std;
 int main (){
 	int t; cin>>t;
 	long n,pre,curr;
 	int c=1;
 	while(t--){
 		cin>>n;
 		pre=curr=n;
 		int digits[10]={0};
 		int flag=0;
 		int flag1=0;
 		int i=1;
 		int dig_count=0;
 		long z=curr;
		while(z>0){
			digits[z%10]=1;
			z/=10;
		} 			
				
 		do{
	 		pre=curr;
 			curr = (i+1)*n;
 			long z=curr;
 			while(z>0){
 				digits[z%10]=1;
 				z/=10;
 			}
 			dig_count=0;
 			for(int k=0;k<10;k++){
 				if(digits[k]==1)
 					dig_count++;
 			}
 			if(dig_count==10){
 				flag1=1;
 				break;
 			}
 			i++;
 			//cout<<"pre "<<pre<<"curr"<<curr<<endl;
 		}while(pre!=curr);
 		if(flag1==0){
 			cout<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;	
 		}
 		else
	 		cout<<"Case #"<<c<<": "<<curr<<endl;
 		c++;
 	}
	return 0;
 }
