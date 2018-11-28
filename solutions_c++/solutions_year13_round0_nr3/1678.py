#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<sstream>
#define MAX_N 10000000
using namespace std;

bool is_palindrome(int n){
	/*if(n>MAX_N){
		cout<<"cuadrado: "<<n<<endl;
		cout<<"we: "<<we<<endl;
	}*/
	int copia=n;
	vector<int> rever;	 	
	while(n>0){
		rever.push_back(n%10);		
		n/=10;
	}
	bool sirve=true;
	for(int i=0; i<(rever.size()/2) && sirve; i++){
		if(rever[i]!=rever[rever.size()-i-1])
			sirve=false;
	}
	if(!sirve)
		return false;
	double to_s=pow(copia,2.0);	
	std::ostringstream strs;
	strs<<fixed;
	strs<<to_s;
	std::string	s= strs.str();	
	string s_r="";
	sirve=true;
	for(int i=0; i<s.length(); i++){
		if(s[i]=='.')
			break;
		s_r+=s[i];
	}
	//cout<<"s_r es: "<<s_r<<endl;
	for(int i=0; i<(s_r.length()/2) && sirve; i++){
		if(s_r[i]!=s_r[s_r.length()-i-1])
			sirve=false;
	}
	return sirve;
	
}

int main(){
	//freopen("c.out","w",stdout);		
	map<int,bool> sirve;		
	for(int i=1; i<=MAX_N; i++){		
		if(is_palindrome(i)){
			//cout<<"i: "<<i<<" sirve"<<endl;		
			sirve[i]=true;
		}
	}
	//cout<<"termine llenado de sirve"<<endl;
	int cuenta=0;
	map<int,int> num;
	for(int i=1; i<=MAX_N; i++){
		if(sirve[i])
			cuenta++;
		num[i]=cuenta;
	}
	//cout<<"termine llenado de cuenta"<<endl;	
	int tc;
	double a,b;
	int r_a,r_b;
	while(1){	
	cin>>tc;
	for(int c=1; c<=tc; c++){
		cin>>a>>b;
		a=sqrt(a);
		b=sqrt(b);
		/*cout<<"a es: "<<a<<endl;
		cout<<"b es: "<<b<<endl;*/
		if((int)a==a)
			r_a=(int)a -1;		
		else
			r_a=floor(a);		
		/*cout<<"r_a: "<<r_a<<" r_b: "<<b<<endl;
		cout<<"num en r_a: "<<num[r_a]<<" num en r_b: "<<num[b]<<endl;*/						
		cout<<"Case #"<<c<<": "<<(num[b] - num[r_a])<<endl;
	}
	}
}
