#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

int main(int argc, char **argv){
	
	if(argc<2){
		std::cout<<"Enter filename\n";
		return(0);
	}	
	char *file = argv[1];
	ifstream infile(file);
	int n;
	infile>>n;
	int a;
	string b;
	int total;
	int ctr;
	int c =0;
	while(infile >>a >> b){
		total = 0;
		ctr = 0;
		for(int i=0;i<=a;i++){
			while(i>total){
				ctr++;
				total++;
					
			}
			total += b[i]-'0';
		}
		cout<<"Case #"<<++c<<": "<<ctr<<endl;	
	}

}

