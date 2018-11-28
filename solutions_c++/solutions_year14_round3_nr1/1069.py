#include <cstdio>
#include <fstream>
#include <string>
#include <cstdlib>
#include <iostream>
using namespace std;


int main(){
	int cases, n;
	ifstream input;
	ofstream output;
	input.open("A-large.in");
//	output.open("output.txt");
	int c,i,j,f,gen;
	long long int p,q,r,q1,t;
	char s;
	input>>cases;
//	cout<<cases<<'\n';
	for(c=0;c<cases;c++){
		input>>p>>s>>q;
//		cout<<p<<s<<q<<'\n';
		gen=0;
		q1=q;
		f=0;
		while(q1%2==0){
			q1=q1/2;
		}
//		cout<<q1<<'\n';
		if(q1!=1){
			if(p%q1!=0){
				cout<<"Case #"<<c+1<<": impossible\n";
				f=1;
			}
			else{
				p=p/q1;
				q=q/q1;
			}
		}
//		cout<<p<<q<<'\n';
		if(!f){
			t=1;
			while(t<1*(q*1.0/(p*1.0))){
				gen++;
				t=t*2;
			}
			cout<<"Case #"<<c+1<<": "<<gen<<'\n';
		}
	}
	
	input.close();
	output.close();
	return 0;
}