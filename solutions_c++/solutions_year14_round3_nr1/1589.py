#include <iostream>
#include <string>
#include <algorithm>
#include <stdio.h>
using namespace std;

long long int pow(long long int a){
	long long int count=0;
	while(a/2!=0){
		
		
	count++;
	a/=2;
	}
return count;
}


long long int pow2(long long int a){
	long long int count=0;
	while(a/2!=0){
		
		if(a%2!=0)
			return -1;
	count++;
	a/=2;
	}
return count;
}


 int main(){
freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	long long int t,p,q,count,i,f,g,nt=0;
	cin>>t;
	string s;
	while(t--){
			nt++;
		cout<<"Case #"<<nt<<": ";
		cin>>s;
		p=0;
		q=0;
		f=0;
		for(i=0;i<s.size();i++){
			if(s[i]!='/'&&f==0){
			p = p * 10+ (s[i]-'0');
			
		}
			else if(s[i]=='/')
				f=1;
			else if(s[i]!='/'&&f==1)
				q=q*10+(s[i]-'0');
		}
		if(p>q)
			cout<<"impossible"<<endl;
		else if(p==q)
			cout<<"0"<<endl;
		else{
		g=std::__gcd(p,q);
		p/=g;
		q/=g;
		//cout<<p<<q;
		
		
			//cout<<pow2(q);
			if(pow2(q)==-1)
				cout<<"impossible"<<endl;
			else{
				cout<<pow2(q)-pow(p)<<endl;
			}
		}
	
	}

	return 0;
}