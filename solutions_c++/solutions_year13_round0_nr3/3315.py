#include<iostream>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

bool isPalindrome(int n)
 {
    int i,j,m,p=1,d,c;
	m=n;
	c=0;
	while(n>0) {
		n/=10;
		p*=10;
	}
	p/=10;
	n=m;
	while(n>0) {
		d = n%10;
		c += (p*d);
		p/=10;
		n/=10;
	}
		//cout<<m<<" "<<c<<endl;
		if(m==c){ return true;}
		else
			return false;
 }
bool isSquare(int n)
 {
   	
	for(int i=1;i*i<=n;i++) {
		if((i*i)==n) {
			if(isPalindrome(i)) return true;
		}
	}
			return false;
 }

int main()
{

	int i,j,k,n,c,m,t,dot,x,z,ans;

	cin>>t;
	
	for(k=1;k<=t;k++) { 
		c=0;
		cin>>m>>n;
		
		for(i=m;i<=n;i++) {
			
			if(isPalindrome(i)) {
				if(isSquare(i)) { c++; }
			 }
		  }
		cout<<"Case #"<<k<<": "<<c<<endl;
	}
		
	
	return 0;
}

