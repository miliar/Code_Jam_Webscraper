/******************************************************************************
Author: Jonathan Lam
Project Name: fs.cpp
Compiler: Dev C++
Due Date: 5/12/2012
******************************************************************************/
#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <math.h>
#include <sstream>

using namespace std;

bool CheckSquare(int i);
bool CheckPal(int i);

int main()
{    
    ifstream file;
    ofstream ofile;
    int trials = 0;
    string num;
    int low, high, root;
    int total;
    
    file.open("a.in");
    ofile.open("answer.in");    
    
    file >> trials;
    
    for (int i = 0; i < trials; i++)		
    {
    	file >> low;
    	file >> high;
    	total = 0;
		for (int x = low; x <= high; x++)		//Start counting
		{
			if (CheckSquare(x))					//Check for perfect square
				if (CheckPal(x))					//Check if palindrome
				{
					root = sqrt(x);
					if (CheckPal(root))
						total++;
				}
			
						
		}				
	    	
    	ofile<<"Case #"<<i+1<<": "<<total<<endl;	
    }
	
	
	  
    file.close();
    ofile.close();
    return 0;
}

bool CheckSquare(int i)
{
	double square = sqrt(i);
	int squareint = square;
	if (square == squareint)
		return true;	
	else
		return false;
}

bool CheckPal(int i)
{
	int sum;
	stringstream ss;
	ss << i;
	string num = ss.str();						//Convert to string
	
	if (num.size() == 1)
		return true;
	
	string first = "";
	string last = "";
	
	for (int j = 0; j < num.size()/2; j++)	
	{
		sum = num[j] - num[num.size()-j-1];
		if (sum != 0)
			return false;					
	}	
	return true;
}
















