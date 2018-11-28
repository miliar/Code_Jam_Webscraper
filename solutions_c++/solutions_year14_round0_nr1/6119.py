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
	for(int t = 0 ; t < T; t++){
		map<int, int> vm;
		int r,val;
		ifile>>r;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				ifile>>val;
				if(i==r-1){
					vm[val]=0;
				}
			}
		}
		ifile>>r;
		int found = 0;
		int fval = -1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				ifile>>val;
				if(i==r-1 && vm.find(val)!=vm.end()){
					fval = val;
					found++;
				}
			}
		}
		PrintCase(t+1);
		if(found == 1){
			cout<<fval;
		}else if (found > 1){
			cout<<"Bad magician!";
		}else if(found == 0){
			cout<<"Volunteer cheated!";
		}
		cout<<endl;
	}//Case loop
}