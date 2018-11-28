#include<iostream>
#include<fstream>
#include<cstring>

inline int toInt(char in){
	return in-48;
}

int main(){
	std::ifstream myFile;
	myFile.open("1_input.txt");
	if(!myFile.is_open()){
		std::cout<<"reading error\n";
		return 0;
	}
	int cases=-1;
	myFile>>cases;	
	for(int ii=1;ii<=cases;++ii){
		int size=-1;
		myFile>>size;
		std::string auds;
		myFile>>auds;
		int result=0;
		if(auds[0]=='0'){
			++result;
			auds[0]='1';
		}
		for(int jj=1;jj<auds.size();++jj){
			if(auds[jj-1]-48<jj&&auds[jj]!='0'){
				result+=jj-auds[jj-1]+48;
				auds[jj]+=jj-auds[jj-1]+48;
			}
			auds[jj]+=auds[jj-1]-48;
		}
		std::cout<<"Case #"<<ii<<": "<<result<<std::endl;
	}
	return 0;
}