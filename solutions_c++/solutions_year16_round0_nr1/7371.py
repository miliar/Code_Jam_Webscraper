#include<iostream>
#include <fstream>
std::ifstream infile("thefile.in");
std::ofstream offile("out.txt");
using namespace std;
long long a[10];
void blank(long long a[]){
	  for(long long i=0;i<10;i++){
   	a[i]=0;
   	
   }
 
}
void operate(long long n){
	 long long d;
	 while (n!=0)
   {
      d= n%10;
    a[d]++;
      n/=10;
   }
}
bool check(long long a[]){
	long long c=0;
	  for(long long i=0;i<10;i++){
   	if(a[i]>=1){
   		c++;
   		
   	}
   	
   }
   if(c==10){
   	return true;
   	
   }else return false;
	
}

int main(){
	 long long t,n;
	infile>>t;
	for(long long y=0;y<t;y++)
	 {blank(a); 
	 
	 long long i=1;
	    infile>>n;
	    if(n==0){
	    	offile<<"Case #"<<y+1<<": INSOMNIA"<<endl;
	    }else{
	    
	    long long temp=n;
	     while (1){
	     
	     	 operate(n*i);
	       	if(check(a)){
	       		break;
	       	}
	     	i++;
	     }
	
	      offile<<"Case #"<<y+1<<": "<<n*i<<endl;}
	  	}
	return 0;
}
