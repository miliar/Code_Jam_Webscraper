#include <iostream>
#include <string>
using namespace std;
int t,c[27],d[10];
string s;

void p(){
	int x;
	if(c[int('U') - 64]){
		x = c[int('U') - 64];
		d[4]+=x;
		c[int('F') - 64]-=x;
		c[int('O') - 64]-=x;
		c[int('U') - 64]-=x;
		c[int('R') - 64]-=x;
	}
	if(c[int('F') - 64]){
		x = c[int('F') - 64];
		d[5]+=x;
		c[int('F') - 64]-=x;
		c[int('I') - 64]-=x;
		c[int('V') - 64]-=x;
		c[int('E') - 64]-=x;
	}
	if(c[int('X') - 64]){
		x = c[int('X') - 64];
		d[6]+=x;
		c[int('S') - 64]-=x;
		c[int('I') - 64]-=x;
		c[int('X') - 64]-=x;
	}
	if(c[int('V') - 64]){
		x = c[int('V') - 64];
		d[7]+=x;
		c[int('S') - 64]-=x;
		c[int('E') - 64]-=x;
		c[int('V') - 64]-=x;
		c[int('E') - 64]-=x;
		c[int('N') - 64]-=x;
	}
	if(c[int('Z') - 64]){
		x = c[int('Z') - 64];
		d[0]+=x;
		c[int('Z') - 64]-=x;
		c[int('E') - 64]-=x;
		c[int('R') - 64]-=x;
		c[int('O') - 64]-=x;
	}
	if(c[int('G') - 64]){
		x = c[int('G') - 64];
		d[8]+=x;
		c[int('E') - 64]-=x;
		c[int('I') - 64]-=x;
		c[int('G') - 64]-=x;
		c[int('H') - 64]-=x;
		c[int('T') - 64]-=x;
	}
	if(c[int('H') - 64]){
		x = c[int('H') - 64];
		d[3]+=x;
		c[int('T') - 64]-=x;
		c[int('H') - 64]-=x;
		c[int('R') - 64]-=x;
		c[int('E') - 64]-=x;
		c[int('E') - 64]-=x;
	}
	if(c[int('T') - 64]){
		x = c[int('T') - 64];
		d[2]+=x;
		c[int('T') - 64]-=x;
		c[int('W') - 64]-=x;
		c[int('O') - 64]-=x;
	}
	if(c[int('O') - 64]){
		x = c[int('O') - 64];
		d[1]+=x;
		c[int('O') - 64]-=x;
		c[int('N') - 64]-=x;
		c[int('E') - 64]-=x;
	}
	if(c[int('I') - 64]){
		d[9]+=c[int('I') - 64];
	}
}

void q(){
	for(int j=0; j<10; j++){
		while(d[j]){
			cout<<j;
			d[j]--;
		}
	} 
}

int main() {
	
	cin>>t;
	for(int i=1; i<=t; i++){
		cin>>s;
		for(int j=0; j<27; j++){
			c[j]=0;
		}
		for(int j=0; j<s.length(); j++){
			c[int(s[j]) - 64]++;
		}
		for(int j=0; j<10; j++){
			d[j]=0;
		}
		p();
		cout<<"\nCase #"<<i<<": ";
		q();
	}
	return 0;
}
