#include<iostream>
#include<cstdio>
#include<cstring>
#include<iomanip>
using namespace std;

int main() {
	//freopen("B-small-attempt0.in", "r", stdin);
    //freopen("output1.txt", "w", stdout);
    long int n;
    int a,b,k,t;
    long int count;
    cin>>t;
    int r=0;
    
    while(t--) {
		cin>>a>>b>>k;
		   count=0;
		   r++;
           for(int i=0;i<a;i++){
           
              for(int j=0;j<b;j++) {
					n=i & j;
					if(n<k)
					count++;
					
					
					
					}
              }
              cout<<"Case #"<<r<<": "<<count<<"\n";
		
		}
		
		
}
    
    
    

