#include<iostream>

using namespace std;
int iscount(int []);
int main(void){
	
	
	 int test;
	cin>>test;
	long ans[test];
	for(int i=0;i<test;i++){
		
		
		long n,no;
		int coun,count;
		
		cin>>n;
		if(n==0){
			ans[i]=0;
			
		}else{
		
		    int a[10];
		    
		    for(int j=0;j<10;j++){
		    	a[j]=0;
		    	
		    }
		    int m=1;
		    int c=10;
		    
		    while(!iscount(a)){
		    	no=m*n;
		    	
		    	long temp;
		    	temp=no;
		    	while(temp!=0){
			    	int coun=temp%c;
			    	a[coun]=1;
			    	temp=temp/c;
		    	}
		    	m++;
			}
	    	ans[i]=no;
		}
		
		
	
		
		
	}
	
	for(int i=0;i<test;i++){
		if(ans[i]==0){
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}else{
			cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
		}
		
	}
	
	
/*	int n=1;
	int c=n%10;
	cout<<c;	long k=1000000;
	cout<<k;
	*/
	

	
}

int iscount(int a[]){
	
	for(int i=0;i<10;i++){
		if(a[i]==0){
			return 0;
		}
	}
	return 1;
	
}