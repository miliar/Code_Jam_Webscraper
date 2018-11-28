#include<iostream>
#include<string>
#include <sstream>

using namespace std;
long long int ret_fac(long long int a){
	long long int x=0;
	while(a!=1){
		if(a%2 !=0)
			return -1;
		x++;
		a=a/2;
		}
	return x;
	}
long long int asd(long long int a){
	long long int x=2, s=0;
	
	while(a>=x){
		x=x*2;
		s++;
		}
	return s;
	}
int main(){
	
	long long int factor, test,ans, p, q, check;
	string s;
	char a;
	cin >> test;
	for(long long int i=0; i < test; i++){
		cin >> p;
		cin >> a;
		cin >> s;
		check=0;
		ans=0;
	    stringstream(s) >> q ;
/*		if(q%p!=0 && q%2!=0){
			cout << "Case #"<<i+1<<": impossible"<< endl; 
			continue;Case #1: 5
		}
	*/    if(q%p==0){
			q=q/p;
			p=1;
		}
		factor=ret_fac(q);
		if(factor==-1){
			cout << "Case #"<<i+1<<": impossible"<< endl; 
			continue;
			}
		if(p==1){
			cout << "Case #"<<i+1<<": "<< factor << endl;
			continue;
			}
		p=asd(p);	
		cout << "Case #"<<i+1<<": "<< factor-p<< endl;
		}
	return 0;
	}

