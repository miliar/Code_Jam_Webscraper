#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
bool palindrome(int a) {
	int r=a;
	int x=0;
	while(a>0) {
		x=x*10 + a%10;
		a/=10;
	}
	//cout<<x<<" "<<a<<endl;
	if(x==r)
	return true;
	return false;
}
int main() { 
int t; 
cin>>t; 
int iter=1;
while(t--) {
	int a,b; 
	cin>>a>>b;
	int count=0;
	for(int i=a;i<=b;i++) {
		int s = sqrt(i);
		if(s*s!=i) {
			continue;
		}
		if(palindrome(i) && palindrome(s))
		count++;
	}
	cout<<"Case #"<<iter<<": "<<count;
	iter++;
	if(t!=0)
	cout<<endl;
}
}
