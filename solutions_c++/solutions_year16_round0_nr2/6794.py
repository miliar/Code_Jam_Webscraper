#include <iostream>
#include<algorithm>
#include<string.h>
using namespace std;
 
int main() {
	// your code goes here
	int t;
	cin>>t;
	int n=t;
	while(t--){
		string a;
		int x=0;
		cin>>a;
		a[a.length()]='0';
		for(int i=0;i<a.length()-1;i++){
		    if(a[i]=='+' && a[i+1]=='-')
		    x++;
		}
		if(a[0]=='-')
		cout<<"Case #"<<n-t<<":"<<" "<<2*x+1<<"\n";
		else
		cout<<"Case #"<<n-t<<":"<<" "<<2*x<<"\n";
	}
	return 0;
} 