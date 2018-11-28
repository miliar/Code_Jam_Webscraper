#include <iostream>
#include <fstream>

using namespace std;

bool isCons(char &c){
	switch (c){
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u': return false; break;
		default: return true; 
	}
}

int main (){
	
	ifstream in("A-small-attempt0.in");
	ofstream cout("output.txt");
	int T; in>>T;
	for (int t=1; t<=T; t++){
		
		cout<<"Case #"<<t<<": ";
		
		string s; in>>s;
		int n; in>>n;
		
		int last=0, substrings=0;
		bool cons;
		for (int i=0; i<s.length()-n+1; i++){
			cons=true;
			for (int j=0; j<n; j++){
				if(!isCons(s[i+j])){
					cons=false; break;
				}
			}
			//is cons
			if(cons){
				substrings+=(i-last+1)*(s.length()-i-n+1);
				last=i+1;
			}
			
		}
		
		cout<<substrings;
		cout<<"\n";
	}
	
	return 0;
}
