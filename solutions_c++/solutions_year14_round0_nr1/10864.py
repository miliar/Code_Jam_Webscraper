#include <iostream>
#include <cstdio>
#include <algorithm>
#include<set>
#include <fstream>

using namespace std;

int main(){
	ifstream in;
	ofstream out;
	in.open("A-small-attempt1.in");
	out.open("A-small-attempt1.out");
	int t, x, help, val, y;
	in>>t;
	for(int i=1; i<=t; i++){
		set<int> zb;
		help=0;
		in>>x;
		for(int j=0; j<4; j++){
			for(int n=0; n<4; n++){
				in>>y;
				if(j==x-1){
					zb.insert(y);
				}
			}
		}
		in>>x;
		for(int j=0; j<4; j++){
			for(int n=0; n<4; n++){
				in>>y;
				if(j==x-1){
					if(zb.find(y) != zb.end()){
						help++;
						val=y;
					}
				}
			}
		}
		out <<"Case #"<<i<<": ";
		if(help==1){
			out<<val<<"\n";
		}
			else if(help==0){
				out<<"Volunteer cheated!\n";
			}
				else{
					out<<"Bad magician!\n";
				}
	}
	out.close();
	in.close();
	return 0;
}
				
		
		
		
		