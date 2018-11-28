#include<iostream>
using namespace std;

int main(){
	int k,m,t,counter,b;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>k>>m;
		cout<<"Case #"<<counter<<": ";
		if(k>0){
			for(b=0;b<k;++b)
				cout<<"WE";
		}
		else{
			for(b=0;b>k;--b)
				cout<<"EW";			
		}
		if(m>0){
			for(b=0;b<m;++b)
				cout<<"SN";
		}
		else{
			for(b=0;b>m;--b)
				cout<<"NS";			
		}
		cout<<endl;
	}
}
