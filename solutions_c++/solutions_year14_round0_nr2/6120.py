#include<iostream.h>
#include<fstream>
using namespace std;
main()
{
	
	;
	double Case;
	ifstream in("B-large.in");
	ofstream out("output.txt");
	out.precision(7);
	out.setf(std::ios::fixed, std::ios::floatfield);
	in>>Case;

	for(int i=0;i<Case;i++)
	{
		double coki=0.0,cokineed;
	double sec=0.0;
	double coki2=2.0;
	double cokifarmes;
	double xtracoki,counter=0.0;
	in>>cokifarmes;
	in>>xtracoki;
	in>>cokineed;		
	if(cokineed<cokifarmes)
		{
			
		out<<"Case #"<<i+1<<": "<<cokineed/2.0<<endl;	
		sec=coki/2;
		}
		else{
			
		
		sec=cokifarmes/coki2;
		coki=cokifarmes;
	while(1)
	{
		double way1,way2;
		way1=cokineed-cokifarmes;
		way1/=coki2;
		
		way2=cokineed/(coki2+xtracoki);
		if(way1<way2)
		{
		sec+=way1;
		out<<"Case #"<<i+1<<": "<<sec<<endl;
		break;	
		}
		else
		{
			coki=0.0;
			coki2+=xtracoki;
			sec+=(cokifarmes/coki2);
			
		}
		
	}
	
	}
		
			
		
		
		
		
	}
	
}