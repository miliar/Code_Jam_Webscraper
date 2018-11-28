#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <Math.h>

double n=0;
double m=0;

double Root(double n){
	return sqrt(n);
}

bool isSquare(double n){
	double r=sqrt(n);
	if( r==floor(r) )
	    return true;
 	return false;
}

bool isPal(double n){
    int num=0;// numero de decimales
	for(int i=1; i<=n;i*=10) num++;
	
	for(double i=0;i<floor(num/2); i=i+1){
		double d1=n, d2=n, aux;
		
		for(double j=0; j<num-i-1; j=j+1)
			d1=(d1/10);
		d1=floor(d1);
		aux=floor(d1/10)*10;
		d1=d1-aux;
		for(double j=0; j<i; j=j+1)
			d2=(d2/10);
		d2=floor(d2);
		aux=floor(d2/10)*10;
		d2=d2-aux;
		
		//std::cout<<";"<<d1<<" "<<d2<<";";

	    if( d1==d2 )continue;
	    else {
			return false;
		}
	}
	return true;
}

int Analize(double n){
	if( isPal(n) && isSquare(n) && isPal(Root(n)) )
		return 1;
	return 0;
}

int main(){
	int Testcases=0;
	double TOTAL=0;
	std::string line;

	std::ifstream ifs ( "test.in" , std::ifstream::in );
	std::ofstream ofs ( "test.out" , std::ifstream::out );

	ifs >> Testcases;
	std::getline( ifs, line);
	for ( int i=0; i<Testcases;++i ){
		TOTAL=0;
		ifs>>n>>m;

		for(double j=n; j<=m; j=j+1)
			TOTAL+=Analize(j);

		ofs<<"Case #"<<i+1<<": "<< TOTAL <<std::endl;

	}

	ifs.close();
	ofs.close();

	//std::cin.get();
}
