#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include <algorithm>

using namespace std;

//	getline(ifile,s); //remove prev lines <- Read A Line

vector<string> SplitString(string inputStr, char delimiter=' '){
	vector<string> sv;
	string s;
	for(int i=0; i<inputStr.length(); i++){
		if(inputStr[i]==delimiter){
			sv.push_back(s);
			s.clear();
		}else{
			s.append(1,inputStr[i]);
		}
	}
	if(!s.empty()){
		sv.push_back(s);
	}
	return sv;
}

void PrintCase(int t){
	cout<<"Case #"<<t<<": ";
}


int T;

int main(int argc, char *argv[]){
	ifstream ifile;
	ifile.open(argv[1]);
	ifile>>T;
	for(int t = 0; t < T; t++){
		double c,f,x;
		ifile>>c>>f>>x;
		double currentC=0.0;
		double currentR=2.0;
		double time=0.0;
		if(c>x)c=x;
		while(currentC<x){
			//cout<<currentC<<endl;
						
			if(currentC<c){
				//cout<<"m"<<endl;
				time+=(c-currentC)/currentR;
				currentC = c;
				continue;
			}
			
			if((x-currentC)/currentR > (x-currentC+c)/(currentR+f)){
				//cout<<"v"<<endl;
				currentC-=c;
				currentR+=f;
			}else{
				time+=(x-currentC)/currentR;
				break;
			}
		}
		PrintCase(t+1);
		printf("%0.7f ",time);
		cout<<endl;
	}//Case loop
}