#include <iostream>
#include <fstream>
using namespace std;

int main () {
  ofstream myfile;
  ifstream input;
  input.open("file.in");
   myfile.open ("example.txt");
   
	int n;
	input>>n;
	for(int i=1; i<=n; i++){
		int a, b;
		int r1[5], r2[5];
		input>>a;
		for(int x=1; x<=4; x++){
			for(int y=1; y<=4; y++){
			input>>b;
			if(x==a)r1[y]=b;
		}
		}
		input>>a;
		for(int x=1; x<=4; x++){
			for(int y=1; y<=4; y++){
			input>>b;
			if(x==a)r2[y]=b;
		}
		}
		int count=0;
		for(int x=1; x<=4; x++){
			for(int y=1; y<=4; y++){
				if(r1[x]==r2[y]){
					count ++;
					a=r1[x];
				}
			}
		}
		if(count==0){
			myfile<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}else if(count ==1){
			myfile<<"Case #"<<i<<": "<<a<<endl;
		}else{
			myfile<<"Case #"<<i<<": Bad magician!"<<endl;
		}
	
	
	}
   
   
   

   
   
   
   
  myfile.close();
  input.close();
  return 0;
}
