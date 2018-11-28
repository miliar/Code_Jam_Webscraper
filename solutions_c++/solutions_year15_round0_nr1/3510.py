#include<iostream>
#include<fstream>
#include<string>
using namespace std;

#define ll long long

int main(){
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("Q1_output.txt");
	
	ll t;
	
	input>>t;
	ll tot=t;
	while(t--){
		ll n;
		ll cnt=0,avl=0;
		
		input>>n;
		for(ll i=0;i<=n;i++){
			char y;
			ll yin;
			input>>y;
			yin=y-'0';
			if(yin!=0){
				if(i<=avl) avl+=yin;
				
				else{
					cnt+=i-avl;
					ll x=i-avl;
					avl+=(x+yin);
				}
			}
		}
		output<<"Case #"<<tot-t<<": "<<cnt<<endl;
	}
	input.close();
	output.close();
	return 0;
}
