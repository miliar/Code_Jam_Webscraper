#include<iostream>
#include<set>
using namespace std;
int t,p,k,i,j;
long n,m,temp;
int main(){
	cin>>t;
	j=0;
	while(t){
	set<int> myset;
	cin>>n;
	++j;
	if(n==0){
	
		cout<<"Case #"<<j<<": INSOMNIA"<<endl;
	}
	else{
		
		p=1;
		i=1;
		m=n;
		while(p){
			n= i*m;
			temp = n;
			++i; 
			while(n){
				k=n%10;
				n=n/10;
				myset.insert(k);
				
				
				if(myset.size()==10){
					p=0;
					break;
				}
				
			}
			
		
		
		}
		cout<<"Case #"<<j<<": "<<temp<<endl;
	
	}
	
	myset.clear();
	--t;}




	return 0;
}
