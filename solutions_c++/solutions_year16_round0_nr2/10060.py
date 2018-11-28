
#include<iostream>
#include<string.h>
using namespace std;


int flip(int *stack){
	int N=0;
	int i=0,j=0;
	int l;
	
	int c=0;
	for(int n=0;n<100;n++)c=c+stack[n];
	if(c>=100) return 0;
	
	if(stack[0]==0){
		i=0;
		while(stack[i]==0 && i<100) i++;
		for(int j=0;j<i;j++) stack[j]=1;
					
		return 1;
	}else{
		
		i=0;
		while(stack[i]==1 && i<100) i++;
		j=i;
		while(stack[j]==0 && j<100) j++;
		for(int k=i;k<j;k++) stack[k]=1;
		return 2;
		
	}
	
	return 0;
}


int main(void){
	
	int T,N=0;
	long i,j;
	long m=0,num=100;
	cin>>T;
	
	for(i=1;i<=T;i++){
		int stack[100];
		for(int k=0;k<100;k++)stack[k]=1;
		long flips=0;
		char stk[100];
		cin>>stk;
		int len = strlen(stk);
		for(j=0;j<len;j++){
			if(stk[j]=='-')
				stack[j]=0;
		}
		m=0;
		flips=0;
		
		m=flip(stack);	
		flips+=m;
		while(m>0){
				
			m=flip(stack);	
	     	flips+=m;
		}
		
		cout<<"Case #"<<i<<": "<<flips<<endl;
	}
	
	
	return 0;
}
