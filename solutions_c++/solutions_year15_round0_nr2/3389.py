#include<iostream>
#include<fstream>
using namespace std;
#define max 1010
#define ll long long

int main(){
	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("Q2_output.txt");
	
	ll t,tot;
	input>>t;
	tot=t;
	while(t--){
		ll n;
		input>>n;
		int d[max]={0};
		
		for(ll i=0;i<n;i++){
			ll tmp;
			input>>tmp;
			d[tmp]++;
		}
		
		ll min=max;
		ll tmp;
		for(ll i=1;i<max;i++){
			tmp=0;
			for(ll j=i+1;j<max;j++){
				 tmp+= d[j]*((j-1)/i);
			}
			if(tmp+i<min) min=tmp+i;
		}
		output<<"Case #"<<tot-t<<": "<<min<<endl;
	}
	output.close();
	input.close();
	return 0;
}
