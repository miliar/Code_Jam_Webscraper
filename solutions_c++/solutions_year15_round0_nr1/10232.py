#include <iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main() {
	int T,i,N;
	cin>>T;
	for(int x=1;x<=T;x++){
		int sum=0,count=0;
		cin>>N;
		char A[N+2];
		int S[N+1];
	gets(A);
	
	for(i=0;i<N+1;i++){
		S[i]=(int)A[i+1]-48;
//	cout<<S[i]<<" ";
	}
	//cout<<endl;
	for(i=0;i<N;i++){
		
		sum+=S[i];
//	 cout<<sum<<" ";
	    if(sum < i+1){
	    count+= ((i+1)-sum);
	    sum+=((i+1)-sum) ;
	    }
	  //cout<<count<<endl;
	}
		
	cout<<"Case #"<<x<<": "<<count<<endl;	
	}
	return 0;
}