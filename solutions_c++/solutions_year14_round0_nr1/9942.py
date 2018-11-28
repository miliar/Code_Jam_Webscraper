#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

main(){
	int k, a1, a2, jwb;
	int card1[4];
	int card2[4];
	int temp;
	string jawab[100];
	ifstream input ("A-small-attempt2.in");
	input>>k;
	for(int a=0; a<k; a++){
		int x =0;
		int y =0;
		int sama=0;
		input>>a1;
		for(int b=0; b<16; b++){
			if((b<(a1*4))&&(b>=((a1-1)*4))){
				input>>card1[x];
				x=x+1;
			}else{
				input>>temp;
			}
		}
		input>>a2;
		for(int c=0; c<16; c++){
			if((c<(a2*4))&&(c>=((a2-1)*4))){
				input>>card2[y];
				y=y+1;
			}else{
				input>>temp;
			}
		}
		for(int d=0;d<4;d++){
			for (int f=0; f<4; f++){
			if(card1[d]==card2[f]){
				sama=sama+1;
				jwb=card1[d];
			}	
			}
		}
		if(sama==1){
			ostringstream con;
			con<<jwb;
			jawab[a]=con.str();
		}else{
			if(sama==0){
				jawab[a]="Volunteer cheated!";
			}else{				
				jawab[a]="Bad magician!";
			}
		}
		
		
	}
	input.close();
	
	ofstream myfile;
 	myfile.open ("example.txt");
	for(int a=0; a<k; a++){
		if(a==(k-1)){
			myfile<<"Case #"<<a+1<<": "<<jawab[a];
		}else{
			myfile<<"Case #"<<a+1<<": "<<jawab[a]<<endl;
		}	
	}
	myfile.close();
}
