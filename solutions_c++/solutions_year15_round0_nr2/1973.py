/*
 * pancake.cpp
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
std::vector<std::vector<int> > cakenum;
std::vector<int> result;

bool readinput(std::string & filename)
{
    std::ifstream in(filename);
    if(!in)
    {
        std::cout << "Can't read in input file\n";
        return false;
    }
    in >> casenum;
    int dd;
    cakenum.resize(casenum);

    for(unsigned i = 0; i < casenum; ++i)
    {
        in >> dd;
        cakenum[i].resize(dd);
        for(unsigned j = 0; j < dd; ++j)
        {
            in >> cakenum[i][j];
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
        out << "Case #" << i+1 << ": " << result[i] << std::endl;
    }
    return true;

}
int max_element(std::vector<int> & vv)
{
    int maxnum = vv[0];
    for(unsigned i = 1; i < vv.size(); ++i)
    {
        if(vv[i] > maxnum)
            maxnum = vv[i];
    }
    return maxnum;
}
int min_element(std::vector<int> & vv)
{
	int minnum = vv[1];
	if(vv.size() > 2)
		minnum = vv[2];
    for(unsigned i = 3; i < vv.size(); ++i)
    {
        if(vv[i] < minnum)
        {
            minnum = vv[i];
        }
    }
    return minnum;
}
int pancake(std::vector<int> & cakenum)
{
    unsigned dd = cakenum.size();
    if(dd == 0)
    {
        std::cout<< "cakenum size is 0\n";
        return -1;
    }
    std::vector<int> times; // times[i] means if I left i minutes for them to eat how much time they need.
    std::sort(cakenum.begin(), cakenum.end());
    int maxele = cakenum[dd - 1];
    times.resize(maxele + 1);
    times[0] = 0;
    times[1] = 1;
    for(unsigned i = maxele; i >= 2; --i)
    {
        times[i] = i;
        for(int j = dd - 1; j >= 0; --j)
        {
            int addnum = std::max((int)(ceil((double)cakenum[j] / ((double)i)) - 1), 0);
            if(addnum == 0)
                break;
            times[i] += addnum;
        }
    }
    return min_element(times);

}

int main(int argc, char ** argv)
{
    std::string fn = argv[1];
    std::string output = fn.substr(0, fn.find_last_of(".")) + ".out";
    readinput(fn);
    result.resize(casenum);
    for(unsigned i = 0; i < casenum; ++i)
    {
    	if(i==62)
    	{
    		std::cout << "test\n";
    	}
        result[i] = pancake(cakenum[i]);
    }
    writeoutput(output);
}


