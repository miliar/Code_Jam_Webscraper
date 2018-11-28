#include <iostream>
#include <cmath>
#include <fstream>
int findVal(int radius, int paint)
{
	int i=1;
	paint-=2*radius+1;
	std::cout<<"current paint: "<<paint<<'\n';
	if(paint<0)
		return 0;
	return 1+findVal(radius+2,paint);
}
int main(int argc, char* argv[])
{
	if(argc!=3)
	{
		std::cout<<"Needs bullseye <infile> <outfile>";
		return 1;
	}
	std::ifstream inFile(argv[1],std::ios_base::in);
	std::ofstream outFile(argv[2],std::ios_base::out);
	std::cout<<argv[1]<<' '<<argv[2]<<'\n';
	if(!inFile)
	{
		std::cerr<<"Failed to open in";
		return 2;
	}
	int rad;
	int paint;
	int cases;
	int out;
	int circles;
	inFile>>cases;
	std::cout<<cases<<'\n';
	for(int i=0;i<cases;++i)
	{
		inFile>>rad;
		inFile>>paint;
		out=findVal(rad,paint);
		outFile<<"Case #"<<i+1<<": "<<out<<'\n';
		std::cout<<out<<'\n';
	}
	inFile.close();
	outFile.close();
	return 0;//normal exit
}