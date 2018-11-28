#include<iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream myfile;
  	ifstream input;
  	input.open("file.in");
    myfile.open ("saida.txt");
    
	int t;
	input>>t;
	int x, r, c;
	bool ok;
	for(int k=1; k<=t; k++){
		input>>x>>r>>c;	
		
		if(x>7)ok=false;
		else if(x==1){
			ok=true;
		}else if(x==2){
			if((r*c)%2==0)ok=true;
			else ok=false;
		}else if(x==3){
			if((r>=2)&&(c>=2)&&((r*c)%3==0))ok=true;
			else ok=false;
		}else if(x==4){
			if((r>=3)&&(c>=3)&&((r*c)%4==0))ok=true;
			else ok = false;
		}else if(x==5){
			if((r>=3)&&(c>=3)&&((r%5==0)||(c%5==0)))ok=true;
			else ok = false;
		}else if(x==6){
			if((r>=5)&&(c>=5)&&((r*c)%6==0))ok=true;
			else ok = false;
		}
		myfile<<"Case #"<<k<<": ";
		if(ok)myfile<<"GABRIEL"<<endl;
		else myfile<<"RICHARD"<<endl;
	}
	return 0;	
}
