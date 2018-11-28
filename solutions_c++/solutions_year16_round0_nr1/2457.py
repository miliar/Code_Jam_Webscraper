#include <iostream>
#include <fstream>
#include <istream>
#include <ostream>
int sheep(std::istream *in){
	int N;
	int a;
	int b=0;
	*in>>N;
	if(N==0)
		return -1;
	bool seen[10];
	for(int i=0;i<10;++i){
		seen[i]=false;
	}
	while(!(seen[0]&&seen[1]&&seen[2]&&seen[3]&&seen[4]&&seen[5]&&seen[6]&&seen[7]&&seen[8]&&seen[9])){
		++b;
		a=N*b;
		while(a>0){
			seen[a%10]=true;
			a=a/10;
		}
	}
	return N*b;
}
bool runProg(std::istream *in, std::ostream *out){
	//actual contest problem stuff
	int T;
	int a;
	*in>>T;
	for(int i=0;i<T;++i){
		a=sheep(in);
		*out<<"Case #"<<i+1<<": ";
		if(a>0){
			*out<<a;
		}else{
			*out<<"INSOMNIA";
		}
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
