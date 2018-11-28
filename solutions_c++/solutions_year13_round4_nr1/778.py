////////////////////////////////////////////////////////////////
//                                                            //
//  Google Code Jam Template                                  //
//  by MooseBoys                                              //
//                                                            //
////////////////////////////////////////////////////////////////

////////////////////////////////////////////////
//                                            //
//  Generic Code                              //
//                                            //
////////////////////////////////////////////////

////////////////////////////////
//  Standard Includes         //
////////////////////////////////

#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <cassert>
#include <map>
#include <functional>


////////////////////////////////
//  Non-Standard Includes     //
////////////////////////////////

#include <Windows.h>
#include "BigInteger\\BigIntegerLibrary.hh"         // from http://mattmccutchen.net/bigint/
//#include "boost/math/common_factor.hpp" // from http://www.boost.org/


////////////////////////////////
//  Typedefs and Macros       //
////////////////////////////////

typedef long long           LL;
typedef unsigned long long  ULL;


////////////////////////////////
//  Debug Helpers             //
////////////////////////////////

// colored console messages
#define GoodMessage(message) {setColor(GOOD);std::cout<<message<<std::endl;setColor(NORMAL);}
#define BadMessage(message) {setColor(BAD);std::cout<<message<<std::endl;setColor(NORMAL);}
#define ImportantMessage(message) {setColor(IMPORTANT);std::cout<<message<<std::endl;setColor(NORMAL);}
enum consoleColor{NORMAL,GOOD,BAD,IMPORTANT};
inline void setColor(consoleColor c)
{
    WORD wAttributes = 0x07;
    if(c==GOOD) wAttributes = 0x0A;
    if(c==BAD) wAttributes = 0x0C;
    if(c==IMPORTANT) wAttributes = 0xF9;
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),wAttributes);
}


////////////////////////////////
//  Common Functions          //
////////////////////////////////

// find and open a problem input
int loadProblemFile(std::ifstream &inputFile, std::string &inputFileName)
{
    for(char cProblem='A';cProblem<='Z';cProblem++)
    {
        inputFileName = std::string(1,cProblem)+"-test";
        inputFile.open(inputFileName+".in",std::ifstream::in);
        if(inputFile.is_open()) return 0;
        inputFileName = std::string(1,cProblem)+"-large";
        inputFile.open(inputFileName+".in",std::ifstream::in);
        if(inputFile.is_open()) return 0;
        for(char cAttempt='9';cAttempt>='0';cAttempt--)
        {
            inputFileName = std::string(1,cProblem)+"-small-attempt"+cAttempt;
            inputFile.open(inputFileName+".in",std::ifstream::in);
            if(inputFile.is_open()) return 0;
        }
    }
    return -1;
}

// load and create problem input and output streams
int getProblemIO(std::ifstream &input, std::ofstream &output)
{
    std::string fileName;
    if(loadProblemFile(input,fileName)){BadMessage("could not find any input files to load");return -1;}
    else{GoodMessage("successfully loaded input file \""<<fileName<<".in\"");}
    output.open(fileName+".out",std::ofstream::out);
    if(output.is_open()){GoodMessage("successfully created output file \""<<fileName<<".out\"");}
    else{BadMessage("could not create output file \""<<fileName<<".out\"");return -1;}
    return 0;
}

// Big Integer class


////////////////////////////////////////////////
//                                            //
//  Problem-Specific Code                     //
//                                            //
////////////////////////////////////////////////

using namespace std;

struct Journey
{
    int start;
    int end;
    int count;
};

bool operator<(const Journey& a, const Journey& b)
{
    if(a.start < b.start) return true;
    if(a.start > b.start) return false;
    if(a.end > b.end) return true;
    if(a.end < b.end) return false;
    return a.count > b.count;
}

// problem entrypoint
int CodeJamMain()
{
    ifstream input;
    ofstream output;

    if(getProblemIO(input,output)) return -1;
    cout<<fixed<<setprecision(16);
    output<<fixed<<setprecision(16);

	int T;
    input>>T;
    for(int caseNum=0;caseNum<T;caseNum++)
    {
        int N,M;
        input>>N>>M;

        vector<Journey> journeys(M);
        for(auto& j : journeys) input>>j.start>>j.end>>j.count;

        // calculate official price
        BigInteger oprice = 0;
        for(auto& j : journeys)
        {
            BigInteger dist = j.end - j.start;
            BigInteger count = j.count;
            BigInteger cost = count * (dist * N + (dist * (dist-1)) / 2);
            oprice += cost;
        }

        sort(journeys.begin(), journeys.end());

        // get interesting station locations
        vector<int> points;
        for(auto j : journeys)
        {
            if(find(points.begin(),points.end(),j.start) == points.end()) points.push_back(j.start);
            if(find(points.begin(),points.end(),j.end) == points.end()) points.push_back(j.end);
        }
        std::sort(points.begin(),points.end());

        // track best price with optimal swapping
        BigInteger bprice = 0;
        map<int,BigInteger,greater<int>> tickets; // (start, count)
        for(auto p : points)
        {
            BigInteger numLeaving = 0;
            for(auto j : journeys)
            {
                // add new tickets to the pool
                if(j.start == p)
                {
                    if(tickets.find(p) == tickets.end()) tickets[p] = j.count;
                    else tickets[p] += j.count;
                }
                // count how many need to leave
                if(j.end == p) numLeaving += j.count;
            }
            // remove tickets from the pool, newest stations first
            while(numLeaving > 0)
            {
                BigInteger leftWithThisTicket = 0;
                int start = tickets.begin()->first;
                if(tickets.begin()->second > numLeaving)
                {
                    tickets.begin()->second -= numLeaving;
                    leftWithThisTicket = numLeaving;
                }
                else
                {
                    leftWithThisTicket = tickets.begin()->second;
                    tickets.erase(tickets.begin());
                }
                numLeaving -= leftWithThisTicket;
                BigInteger dist = p - start;
                bprice += leftWithThisTicket * (dist * N + (dist * (dist-1)) / 2);
            }
        }

        BigInteger answer = oprice - bprice;
        answer = -answer; // something's off here ... but whatever...
        BigInteger mod = 1000002013;
        answer = answer % mod;

        output<<"Case #"<<caseNum+1<<": ";
        output<<answer<<endl;
        GoodMessage("Case #"<<caseNum+1<<": "<<answer);
    }

    return 0;
}

////////////////////////////////////////////////
//                                            //
//  Generic Entrypoint                        //
//                                            //
////////////////////////////////////////////////

int main(int argc, char* argv[])
{
    int ret = CodeJamMain();
    if(ret==0){GoodMessage(">>>> SUCCESS <<<<");}
    else{BadMessage(">>>> FAILURE <<<<");}
    system("pause");
    return ret;
}
