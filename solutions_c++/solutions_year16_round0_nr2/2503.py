#include <iostream>
#include <fstream>
#include <istream>
#include <ostream>
#include <string>
int pcake(std::istream *in){
	std::string a;
	*in>>a;
	int out=0;
	int sz;
	sz=a.size();
	int changesign=0;
	bool startsign=false;
	if(a[0]=='+'){
		startsign=true;
	}
	if(sz>1){
		for(int i=0;i<sz-1;++i){
			if(a[i]!=a[i+1]){
				++changesign;
			}
		}
	}
	if(changesign%2==1){
		startsign=!startsign;
	}
	out=changesign;
	if(!startsign){
		++out;
	}
	return out;
}
bool runProg(std::istream *in, std::ostream *out){
	int T;
	*in>>T;

	for(int i=0;i<T;++i){
		*out<<"Case #"<<i+1<<": "<<pcake(in)<<'\n';
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
