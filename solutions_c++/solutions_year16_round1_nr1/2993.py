#include <iostream>
#include <cstdio>
#include <vector>
#include <vector>
using namespace std;
int main(){
	// cout<<"Case #"<<k<<": INSOMNIA"<<endl;
	
	int t,n;
	string s,news;
	int a,b;
	cin>>t;
	for (int k=1;k<=t;k++){
		cin>>s;
		n = s.size();
		news = "";
		news = news+s[0];

		for (int i=1;i<n;i++){
			a = s[i]-'A';
			b = news[0]-'A';
			if (a<b){
				news = news+s[i];
			}
			else{
				news = s[i]+news;
			}
		}
		cout<<"Case #"<<k<<": "<<news<<endl;
	}
	
	return 0;
}