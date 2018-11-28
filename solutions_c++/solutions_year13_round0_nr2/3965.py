#include <iostream>
#include <fstream>
//generates output
void sendOut(bool value, std::ofstream &outFile, int caseNum)
{
	outFile<<"Case #"<<caseNum<<": ";
	if(value)
	{
		outFile<<"YES";
	}
	else
	{
		outFile<<"NO";
	}
	outFile<<'\n';
}

//tests case possibility
bool processCase(std::ifstream &inFile)
{
	//declarations
	int height=0;
	int width=0;
	char garbage=0;//holds '\n' for newlines
	int currOffset;
	bool oPut=true;
	bool breakVal=false;
	//pointer declarations
	int* lawn;
	int* rowMax;
	int* columnMax;
	//end decs
	
	//get dimensions of lawn
	inFile>>height;
	inFile>>width;
	//memalloc
	lawn=new int[height*width];
	rowMax=new int[height];//helps judge
	columnMax=new int[width];//helps judge
	//endalloc
	//initialize row/column max
	for(int i=0;i<height;i++)
	{
		rowMax[i]=0;
	}
	for(int i=0;i<width;i++)
	{
		columnMax[i]=0;
	}
	for(int i=0;i<height;i++)//populate lawn, max/min, initialize lawnValidation to false;
	{
		currOffset=i*width;
		for(int j=0;j<width;j++)
		{
			inFile>>lawn[currOffset+j];
			if(lawn[currOffset+j]>rowMax[i])
			{
				rowMax[i]=lawn[currOffset+j];
			}
			if(lawn[currOffset+j]>columnMax[j])
			{
				columnMax[j]=lawn[currOffset+j];
			}
		}
	}
	for(int i=0;i<height&&!breakVal;i++)
	{
		currOffset=i*width;
		for(int j=0;j<width&&!breakVal;j++)
		{
			if(lawn[currOffset+j]<rowMax[i]&&lawn[currOffset+j]<columnMax[j])
			{
				oPut=false;
				breakVal=true;
			}
		}
	}
	//memrelease
	delete[] lawn;
	delete[] rowMax;
	delete[] columnMax;
	//endrelease
	return oPut;
}
//gets number of cases
int getCases(std::ifstream &inFile)
{

	int tmp=0;
	inFile>>tmp;
	return tmp;
}


int main(int argc, char* argv[])
{
	//declarations
	int cases=0;
	//file i/o initial
	
	//get input file name from argument list
	if(argc!=3)
	{
		std::cout<<"start command should read, Lawnmower inputfile outputfile\n";
		return 1;
		
	}
	
	std::ifstream inFile(argv[1],std::ios_base::in);
	std::ofstream outFile(argv[2],std::ios_base::out);

	//parse input file start
	if(!inFile)
	{
		std::cout<<"Cannot open file "<<argv[1] <<" does not exist.\n";
		inFile.close();
		outFile.close();
		return 2;//exits
	}
	//body
	cases=getCases(inFile);
	for(int i=0;i<cases;i++)
	{
		sendOut(processCase(inFile),outFile, i+1);//simple loop, heavy lifting done in functions
	}
	//file i/o close
	inFile.close();
	outFile.close();
	return 0;
}
