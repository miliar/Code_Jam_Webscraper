#include<iostream>
#include<set>
#include<algorithm>
#include<cstdio>
using namespace std;
 
long long int ipl(long long int n){
	set<long long int>s;
	long long int a,b;
        b=0; 
	while(s.size()<10){
		b+=n;
		a=b;
		while(a){
			s.insert(a%10);
			a/=10;
		}
	}
	return b;
}
 
int main() {
	long long int t,n,p=1;
	cin>>t;
	while(t--)
	{
		cin>>n;
		if(n==0) 
		cout<<"Case #"<<p<<":INSOMNIA"<<endl;
		else
		cout<<"Case #"<<p<<":"<< ipl(n)<<endl;
	}
	return 0;
  }