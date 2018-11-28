//#define NDEBUG
#include <thread>
#include <pthread.h>
#include <iostream>
#include <atomic>
#include <vector>
#include <array>
#include <functional>
#include <algorithm>
#include <ctime>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <cmath>
#include <stack>
#include <stdexcept>
#include <list>
#include <queue>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <utility>
#include <unordered_map>
#include <unordered_set>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <assert.h>
#include <typeinfo>
#include <iomanip>

using namespace std;

class testcase
{
    long double C;
    long double F;
    long double X;

    friend class cookie;
};


class cookie
{
    long long T;
    vector<testcase> tests;

public:
    //read the input file and store data in tests and T
    cookie(string infilename)
    {
        //open file
        ifstream infile(infilename);
        assert(infile.good() == true);

        //store data in T and mt;
        infile>>T;
        for(long long i=0;i<T; i++)
        {
            tests.push_back(read_nexttest(infile));
        }
    }

    testcase read_nexttest(ifstream & infile)
    {
        testcase t;

        infile>>t.C;
        infile>>t.F;
        infile>>t.X;

//        cout<<std::fixed<<std::setprecision(7)<<t.C<<" "<<t.F<<" "<<t.X<<endl;
        return t;
    }

    //calculate the answer for test case t
    long double minSec(const testcase & t)
    {
        //find the optimal number of farms we should buy
        //calculate the number of seconds needed
        return minSec(t,nfarms(t));
    }

    //calculate the optimal number of farms to buy
    long long nfarms(const testcase & t)
    {
        return (long long)ceil((t.X / t.C) - (2 / t.F) - 1);

    }

    //calculate the number of seconds needed to buy nfarms plus the last step
    long double minSec(const testcase & t, long long nfarms)
    {
        long double current_ncookies = 2;
        long double sec=0;

        for(long long i=0;i<nfarms;i++)
        {
            //calculate the number of seconds to buy farm i
            sec += (t.C / current_ncookies);

            current_ncookies += t.F;
        }

        sec += (t.X / current_ncookies);

        return sec;
    }

    void run(string outfilename)
    {
        ofstream outfile(outfilename);
        assert(outfile.good() == true);

        //for each test case, make the output
        for(long long i=0;i<T;i++)
        {
            //print the answer in the output file
            printout(outfile, minSec(tests[i]), i+1);
        }
    }

    void printout(ofstream & outfile, long double sec, long long testindex)
    {
//        fprintf(outfile,"Case #%d: %.7f\n",testindex,sec);
        outfile<<std::fixed;
        outfile<<"Case #"<<testindex<<": "<<setprecision(7)<<sec<<"\n";
    }
};


int main(int argc, char * argv[])
{
    cookie c("B-large.in");
    c.run("B-large.out");


	return 0;
}
















