#include <iostream>
using namespace std;
int check();
int seen[10],order[10];
long long n;
int main() {
	long long i,r,j,k=0,T,num,num1,max,index,l,m=0;
	cin>>T;
	for(i=1;i<=T;i++){
	    cin>>n;
	    for(j=0;j<10;j++)seen[j]=order[j]=0;
	    k=0;
	    if(n==0){
	        cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
	        continue;
	    }
	    m=0;
	    while(1){
	    num1=num=n*++m;
	    while(num>0){
	        r=num%10;
	        if(seen[r]==0){
	            order[r]=k++;
	            seen[r]=1;
	        }
	        num=num/10;
	        }
	        if(check())break;
	        
	    }
	    max=order[0];
	    for(l=0;l<10;l++){
	        if(max<order[l]){
	            max=order[l];
	           
	        }
	    }
	    cout<<"Case #"<<i<<": "<<num1<<endl;
	    }
	}
	
int check(){
    int i,j,flag=1;
    for(i=0;i<10;i++)    if(seen[i]==0)return 0;
    return 1;
    }
    
