#include<iostream>
#include<stdio.h>
#include<cstdlib>
#include<cstring>
using namespace std;
int main(){
int t,N,count,i,m,j,p,d;
char k[10];
int a[10];

cin>>t;
for(d=1;d<=t;d++){
	cin>>N;
	count=10;
int flag=0;
	j=2;
	for(i=0;i<10;i++){
	a[i]=0;
	}
	p=N;
	if(N!=0){
	while(p>=N){
		sprintf(k,"%d",p);

		for(i=0;i<strlen(k);i++){
	
			m=k[i];
			if(a[m-48]==0){		
			a[m-48]=1;
			count--;
			}
		
	 	}
		
		p=N*j;
		j++;
		if(count<1){
			flag=1;
			break;		
		}

	
	}
	
	}
	if(flag){
	cout<<"Case #"<<d<<": "<<p-N<<endl;
	}else
	cout<<"Case #"<<d<<": INSOMNIA"<<endl;
}
 
	return 0;
}
