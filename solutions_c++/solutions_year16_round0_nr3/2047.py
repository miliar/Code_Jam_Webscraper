#include <iostream>
#include <fstream>
#include <istream>
#include <ostream>
#include <vector>
int powrem(int num, int modprime, int exponent){
	
	if(exponent==0)
		return 1;
	int rem=num%modprime;
	if(rem<2)
		return rem;
	if(exponent%2>0)
		return rem*powrem(rem*rem,modprime,exponent/2)%modprime;
	return powrem(rem*rem,modprime,exponent/2)%modprime;
}
bool getNext(bool *val,int sz){
	bool next=true;
	int i=sz-2;
	while(next&&i>0){
		next=val[i];
		val[i]=!val[i];
		--i;
	}
	return true;
}
bool cjam(std::istream *in, std::ostream *out){
	//given a size n, find j cases where there exists primes p that divide the sum b(i)*a^i where a[2..10] and b(i) is within{0,1}, b(n-1),b(0) are always 1, i within [0..n-1]
	int n;
	int J;

	*in>>n;
	*in>>J;
	int coeff[9]={2,3,4,5,6,7,8,9,10};
	int basePrimes[10]={2,3,5,7,11,13,17,19,23,29};//can be extended
	bool *val=new bool[n];
	val[0]=val[n-1]=true;
	for(int i=1;i<n-1;++i){
		val[i]=false; 
	}
	bool grid[9][10];
	int remgrid[9][10];
	int basegrid[9][10];
	int workgrid[9][10];
	for(int i=0;i<9;++i){//listing of primes that can divide the 
//		std::cout<<"*************************\n";
		for(int j=0;j<10;++j){
			remgrid[i][j]=coeff[i]%basePrimes[j];
			grid[i][j]=(remgrid[i][j]!=0);//the one added makes it impossible
			basegrid[i][j]=powrem(coeff[i],basePrimes[j],n-1)+1;
//			std::cout<<powrem(coeff[i],basePrimes[j],n-1)<<'\n';

		}
	}
	int count=0;
	bool validation[9];

	bool skip;
	while(count<J){
		skip=false;
		for(int i=0;i<9&&!skip;++i){
			validation[i]=false;
			for(int j=0;j<10;++j){
				workgrid[i][j]=basegrid[i][j];
//				std::cout<<i<<' '<<j<<'\n';
//				std::cout<<basegrid[i][j];
				for(int k=1;k<n-1;++k){
					if(grid[i][j]&&val[k]){
						workgrid[i][j]+=powrem(coeff[i],basePrimes[j],n-k-1);
//						std::cout<<'\n'<<powrem(coeff[i],basePrimes[j],n-k-1);
						workgrid[i][j]%=basePrimes[j];
					}
				}
//				std::cout<<'\n';
				workgrid[i][j]%basePrimes[j];
				if(workgrid[i][j]==0||workgrid[i][j]==basePrimes[j]){
					validation[i]=true;
				}
			}
			if(!validation[i]){
				skip=true;
			}
		}//end workgrid
		if(!skip){
			for(int i=0;i<n;++i){
				if(val[i]){
					*out<<'1';
				}else{
					*out<<'0';
				}
			}
			for(int i=0;i<9;++i){
				for(int j=0;j<10&&validation[i];++j){
					if(workgrid[i][j]==0||workgrid[i][j]==basePrimes[j]){
						*out<<' '<<basePrimes[j];
						validation[i]=false;
					}
				}
			}
			*out<<'\n';
			++count;
		}
		getNext(val,n);
	}//endwhile
	return false;
}
bool runProg(std::istream *in, std::ostream *out){
	int n;
	*in>>n;
	for(int i=0;i<n;++i){
		*out<<"Case #"<<i+1<<": "<<'\n';
		cjam(in, out);
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
