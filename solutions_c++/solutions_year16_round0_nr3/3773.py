#include<iostream>
#include<math.h>
#include <stdlib.h>
#include<string.h>
using namespace std;
int isComposite(long long int n,long long int *c,int j){
	int i;
	for(i=2;i<sqrt(n/2);i++){	
		if(n%i==0){
			c[j]=i;		
			return 1;		
		}	
	}
	return 0;
}

int check(char *A){
	int i,flag=0;
		int len = strlen(A);
		long long int base[20]={0};
		long long int divisor[20];
	
		for(int j1=2;j1<=10;j1++){
			base[j1]=0;
			divisor[j1]=0;
			for(int i=0;i<len;i++){
				base[j1]+=(pow(j1,i)*(A[len-i-1]-'0'));
			}
			if(isComposite(base[j1],divisor,j1)==0){
				flag=1;
				break;
			}
		}
		if(flag==0){
		
			cout<<A<<" ";
			for(i=2;i<=10;i++){
				cout<<divisor[i]<<" ";
			}
			cout<<endl;
			return 1;
		}
		else{
			return 0;
		
		}

}


void binary(int n,char A[],int *j,int n1)
{
    if(n < 1){
        if(*j==0||A[0]!='1'||A[n1-1]!='1'){
        	return;
        }
        if(check(A)==1){
        	*j=*j-1;
        
        }
        else{
        	return;
        }
       
    }            
    else
    {
        A[n-1] = '0';
        binary(n-1,A,j,n1);
        A[n-1] = '1';
        binary(n-1,A,j,n1);
    }
}
int main(){
	//isComposite(512);
	int t;
	int num=1;
	cin>>t;
	while(t--){
	
		cout<<"CASE #"<<num<<": "<<endl;
		num++;
		int n,j;
		cin>>n>>j;
		char a[n];
		a[n]='\0';
		binary(n,a,&j,n);
	}
}
