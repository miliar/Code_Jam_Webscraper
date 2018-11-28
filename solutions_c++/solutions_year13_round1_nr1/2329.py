#include <iostream>
#include <fstream>

using namespace std;

int main (){
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");
	int T; in>>T;
	for (int tt=1; tt<=T; tt++){
		int r, t;
		in>>r>>t;
		
		int sum=0;
		int add=((r+1)*(r+1))-(r*r);
		int count=-1;
		
		while (sum<=t){
			sum+=add;
			add+=4;
			count++;
		}
		
		out<<"Case #"<<tt<<": "<<count<<"\n";
	}
	
	return 0;
}
