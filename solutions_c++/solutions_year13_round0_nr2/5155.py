#include <string>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>
#include <vector>
using namespace std;


//the trick is to check whether the two consecutive neighbors of current cell(ex. right and bottom) are larger than itself.
//if so, there is no solution
int main()
{
	string line;
	ifstream myfile("in.txt");
	ofstream outFile;
  	outFile.open ("out.txt");
// get # testcases
  	getline (myfile,line);
	int numCases= atoi(line.c_str());
	int dimX(0), dimY(0);
	for(size_t i = 1; i<= numCases;i++)//numCases; i++)
	{
		bool result = true;
		//getdimensions
		getline (myfile,line);
		std::stringstream stream(line);
		stream >> dimY;
		stream >> dimX;
		vector<int> field[dimY];
		//read lines
		for(int y = 0; y < dimY; y++)
		{
			getline(myfile,line);
			cout<<line<<endl;
			std::stringstream stream1(line);
			while(1)
			{
				int n = 0;
				stream1 >> n;
				if(field[y].size() < dimX)
				{	
					field[y].push_back(n);
				}
				if(!stream1)
					break;
			}
		}
		
		bool bottom(false), up(false),left(false),right(false);
		
		for(int y=0; y<dimY; y++)
		{
			if(y==0)
				up = true;
			 if(y==dimY-1)
				bottom =true;
			
			for(int x = 0; x<dimX; x++)
			{
				if(x == 0)
					left = true;
				 if(x == dimX - 1)
					right = true;

				int value = field[y][x];
		
				// int rightValue(0),leftValue(0),upperValue(0),lowerValue(0);
				
				// upperValue = 0;
				// if(!up)
				// 	upperValue = field[y-1][x];
				// if(!bottom)
				// 	lowerValue = field[y+1][x];
				// if(!right)
				// 	rightValue = field[y][x+1];
				// if(!left)
				// 	leftValue = field[y][x-1];
				
				// if(upperValue > value && rightValue > value)
				// 	result = false;
				// if(upperValue > value && leftValue > value)
				// 	result = false;
				// if(lowerValue>value && rightValue > value)
				// 	result = false;
				// if(lowerValue > value && leftValue > value)
				// 	result = false;
				
				bool hasmoreVertical = false;
				for(int y1 = 0; y1 < dimY ; y1++)
				{
					if(field[y1][x] > value)
						hasmoreVertical = true;
				}
				bool hasMoreHorizontal = false;
				for(int x1 = 0; x1 < dimX; x1 ++)
				{
					if(field[y][x1] > value)
						hasMoreHorizontal = true;
				}

				if(hasmoreVertical && hasMoreHorizontal)
					result = false;


				left=false;
				right = false;
			}
			bottom=false;
			up = false;
		}

		cout<<result<<endl<<"========"<<endl;
		outFile<<"Case #"<<i<<": ";
		if(result)
			outFile<<"YES"<<endl;
		else
			outFile<<"NO"<<endl;
	}
	outFile.close();
	myfile.close();
	return 0;
}