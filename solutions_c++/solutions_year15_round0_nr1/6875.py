#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(void){
	ifstream in("in.txt");
	ofstream out("out.txt");
	
	
	int t;
	in>>t;
	int sMax;
	string s;
	for(int c=1;c<=t;c++){
		int total=0;
		int added=0;
		in>>sMax;
		in>>s;
		
		for(int i=0;i<=sMax;i++){
			if(total>=i)
				total+=(s[i]-'0');
			else{
				int needed=i-total;
				added+=needed;
				total+=needed+(s[i]-'0');
			}
		}
		out<<"Case #"<<c<<": "<<added<<endl;
	}
	
	
	out.close();
	in.close();
}
