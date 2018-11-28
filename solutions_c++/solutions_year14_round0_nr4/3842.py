#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>


class basicAnalizer{
private:
	std::ifstream* ifs;
	
	int n;
	double *S, *H, *S2, *H2;
	
	void readData(){
		*ifs >> n;
		S=new double[n];
		S2=new double[n];
		H=new double[n];
		H2=new double[n];
		for (int i=0; i<n;i++){
			*ifs>> S[i];
			S2[i]=S[i];
		}
		for (int i=0; i<n;i++) {
			*ifs>> H[i];
			H2[i]=H[i];
		}
	}
public:
	basicAnalizer(std::ifstream *ifs):ifs(ifs){ readData();}
	~basicAnalizer(){
		delete[] S;
		delete[] S2;
		delete[] H;
		delete[] H2;
	}
	void doWork(int &p1, int &p2){
		
		int countWar = 0;
		int HPlay=0;
		int min=0;
		int minaux;
		double aux;
		for (int i=0; i<n; i++) {
			HPlay=-1;
			min=-1;
			minaux=-1;
			for (int j=0; j<n-i; j++) {
				if( H[j]>S[i] && (HPlay==-1 || H[j]<H[HPlay]) ){
					HPlay=j;
				}else if(HPlay==-1 && (min==-1 || H[j]<H[min] ) ) {
					min=j;
				}
				if( minaux==-1 || S2[j+i]<S2[minaux] ) {
					minaux=j+i;
				}
			}
			aux=S2[i];
			S2[i]=S2[minaux];
			S2[minaux]=aux;
			
			if(HPlay==-1){
				H[min]=H[n-1-i];
				countWar++;
			}else{
				H[HPlay]=H[n-1-i];
			}
		}	
		
		int countDefWar = 0;
		int H2Play=0;
		int max=0;
		for (int i=0; i<n; i++) {
			H2Play=-1;
			max=-1;
			for (int j=0; j<n-i; j++) {
				if( H2[j]<S2[i] && (H2Play==-1 || H2[j]<H2[H2Play]) ){
					H2Play=j;
				}else if(H2Play==-1 && (max==-1 || H2[j]>H2[max] ) ) {
					max=j;
				}
			}
			std::cout<<std::endl;
			if(H2Play==-1){
				H2[max]=H2[n-1-i];
			}else{
				H2[H2Play]=H2[n-1-i];
				countDefWar++;
			}
		}
			
		p1 = countDefWar;
		p2 = countWar;
	}
};

int main(){
	double r=0;
	int Testcases=0;
	std::string line;

	std::ifstream ifs ( "test.in" , std::ifstream::in );
	std::ofstream ofs ( "test.out" , std::ifstream::out );
	
	ifs >> Testcases;
	std::getline( ifs, line);
	for ( int i=0; i<Testcases;++i ){
		basicAnalizer analizer( &ifs );
		
		int x, y;
		analizer.doWork(x, y);
		
		ofs<<"Case #"<<i+1<<": "<<x<<" "<<y<<std::endl;
	}

	ifs.close();
	ofs.close();

	//std::cin.get();
}
