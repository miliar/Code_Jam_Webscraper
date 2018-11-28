/*
 * dijkstra.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: ni
 */


#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>
//#include <cstdlib>

int casenum;
std::vector<std::vector<int> > input;
std::vector<int> xx;
std::vector<bool> result;

int table[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

bool readinput(std::string & filename)
{
    std::ifstream in(filename);
    if(!in)
    {
        std::cout << "Can't read in input file\n";
        return false;
    }
    in >> casenum;
    input.resize(casenum);
    xx.resize(casenum);
    int stringlen;
    std::string inputstr;
    for(unsigned i = 0; i < casenum; ++i)
    {
    	in >> stringlen >> xx[i];
    	input[i].resize(stringlen);
    	in >> inputstr;
    	for(unsigned j = 0; j < stringlen; ++j)
    	{
    		switch(inputstr[j])
    		{
    		case 'i':
    			input[i][j] = 2;
    			break;
    		case 'j':
    			input[i][j] = 3;
    			break;
    		case 'k':
    			input[i][j] = 4;
    			break;
    		default:
    			std::cout << "unknown input character!\n";
    		}
    	}
    }
    return true;
}

bool writeoutput(std::string & filename)
{
    std::ofstream out(filename);
    if(!out)
    {
        std::cout << "Can't open the output file\n";
        return false;
    }
    for(unsigned i = 0; i < casenum; ++i)
    {
        out << "Case #" << i+1 << ": " ;
        if(result[i])
        	out << "YES";
        else
        	out << "NO";
        out << std::endl;
    }
    return true;

}
int multiply(const int &i, const int & j)
{
	if(i > 0 && j > 0)
	{
		return table[i][j];
	}
	else if(i < 0 && j < 0)
	{
		return table[-i][-j];
	}
	else if(i < 0 && j > 0)
	{
		return -table[-i][j];
	}
	else
	{
		return -table[i][-j];
	}
}

bool dijkstra(std::vector<int> & testcase, int & xx)
{
    unsigned dd = testcase.size();
    if(dd * xx < 3)
    {
        return false;
    }
    std::vector<int> inputmult;
    inputmult.resize(dd);
    inputmult[0] = testcase[0];
    for(unsigned i = 1; i < dd; ++i)
    {
    	inputmult[i] = multiply(inputmult[i-1], testcase[i]);
    }
    std::vector<int> lastmult;
    lastmult.resize(xx);
    lastmult[0] = 1;
    for(int i = 1; i < xx; ++i)
    {
    	lastmult[i] = multiply(lastmult[i-1],inputmult[dd -1]);
    }
    if(multiply(lastmult[xx -1],inputmult[dd-1]) != -1)
    {
    	return false;
    }
    bool findk = false;
    for(int i = xx - 1; i >= 0; --i)
    {
    	for(int j = dd-1; j >=0; --j)
    	{
    		if(!findk)
    		{
    			if(multiply(lastmult[i],inputmult[j]) == 4)
    				findk = true;
    		}
    		else
    		{
    			if(multiply(lastmult[i],inputmult[j]) == 2)
    				return true;
    		}
    	}
    }
    return false;
}

int main(int argc, char ** argv)
{
    std::string fn = argv[1];
    std::string output = fn.substr(0, fn.find_last_of(".")) + ".out";
    readinput(fn);
    result.resize(casenum);
    for(unsigned i = 0; i < casenum; ++i)
    {
        result[i] = dijkstra(input[i], xx[i]);
    }
    writeoutput(output);
}


