#include <iostream>
#include <fstream>
#include <istream>
#include <ostream>
#include <string>

std::string test(std::istream *in,std::ostream *out){
	std::string inputStr;std::string outputStr;
	*in>>inputStr;
	/*
	char* val=new char[inputStr.size()*2];
	int b,c;
	b=inputStr.size();
	c=inputStr.size()+1;
	for(int i=0;i<inputStr.size()*2;++i){
		val=0;
	}
	*(val+b*sizeof(char))=inputStr.at(0);
	for(int i=1;i<inputStr.size();++i){
		if(inputStr.at(i)>=val[b]){
			val[--b]=inputStr.at(i);
		}else{
			val[c++]=inputStr.at(i);
		}
	}
	return &val[b];//will leak like a sieve
	//*/
	//*
	outputStr="";
	std::string a=std::string(1,inputStr.at(0));
	outputStr=a;
	for(int i=1;i<inputStr.size();++i){
		a=std::string(1,inputStr.at(i));
		if(outputStr.at(0)>a.at(0)){
			outputStr.append(a);
		}else{
			outputStr.insert(0,a);
		}
	}
	return outputStr;
	//*/
}
bool runProg(std::istream *in, std::ostream *out){
	int T=0;
	*in>>T;
	for(int i=0;i<T;++i){
		*out<<"Case #"<<i+1<<": "<<test(in,out);
		*out<<'\n';
	}
	return true;
}
int main(int argc, char* argv[]){
	std::istream* iPut;
	std::ostream* oPut;
	std::ifstream iFile;
	std::ofstream oFile;
	
	iPut=&std::cin;
	oPut=&std::cout;
	if(argc==1){
		std::cout<<"This program requires arguments.  "<<argv[0]<<" ifile [0file]\nRunning in debug mode\n";
	}
	if(argc==2){
		iFile.open(argv[1],std::ios::in);
		iPut=&iFile;
	}
	if(argc==3){
		iFile.open(argv[1],std::ios::in);
		oFile.open(argv[2],std::ios::out);
		iPut=&iFile;
		oPut=&oFile;
	}
	if(argc>3){
		std::cerr<<"Too many arguments\n";
		return 1;

	}
	//actual program stuff happens in here
	runProg(iPut, oPut);
	//end program stuff
	if(argc>1){
		iFile.close();

	}
	if(argc>2){
		oFile.close();
	}
	return 0;
}
