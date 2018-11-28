#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <sstream>
using namespace std;

void main(){
	int T, i, j, c[4], d, ctr, result;
	string line,row, line1;
	ifstream myfile;
	ofstream writefile;
	myfile.open("input.in");
	if (myfile.is_open())
	  {
		  if(myfile.good()){
			  getline(myfile, line);
			  T = stoi(line);
		  }
	  }
	else{
		cout<<"Can't open\n";
	}
	writefile.open("hasil.out");
	for(i=1;i<=T;i++){
		ctr=0;
		getline(myfile,row);
		stringstream iss, iss1;	
		for(j=1;j<=4;j++){
			getline(myfile,line);
			if(j==stoi(row)){
				iss << line;
				for(int k=0;k<=3;k++){
					iss >> c[k];
				}
			}
		}
		getline(myfile,row);
		for(j=1;j<=4;j++){
			getline(myfile,line1);
			if(j==stoi(row)){
				iss1<<line1;
				for(int x=0;x<=3;x++){
					iss1 >> d;
					for(int k=0;k<=3;k++){
						if(c[k]==d){
							ctr++;
							result=d;
						}
					}
				}
			}
		}
		
		if(ctr==0){
			writefile << "Case #"<<i<<": Volunteer cheated!"<<endl;
		}
		else if(ctr==1){
			writefile << "Case #"<<i<<": "<<result<<endl;
		}
		else{
			writefile << "Case #"<<i<<": Bad magician!"<<endl;
		}
	}
	myfile.close();
	writefile.close();
}