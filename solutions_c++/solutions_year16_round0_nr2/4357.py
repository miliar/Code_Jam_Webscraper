#include <iostream>
#include <string>
using namespace std;

void flip(string &x,int c){
	for(int i=0; i<=c; i++){
		if(x[i]=='+'){
			x[i]='-';
		}else{
			x[i]='+';
		}
	}
}

int main(){
	int t,l,c,j;
	string x;
	cin>>t;
	for(int i=1; i<=t; i++){
		cin>>x;
		j=0;
		l=x.length();
		cout<<"Case #"<<i<<": ";
		c=l-1;
		for(;c>=0;c--){
			if(x[c]!='+'){
				flip(x,c);
				j++;
			}
		}
		cout<<j<<endl;
	}
	return 0;
}
