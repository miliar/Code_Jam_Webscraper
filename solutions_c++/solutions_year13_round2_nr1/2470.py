#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <map>

using namespace std;

void calc(int ncursize, int ncount, int & osize)
{
     if(ncount == 0)
     {
               osize = 0;
               return;
     }
     osize = ncursize;
     for(int i = 0; i < ncount; ++i)
     {
             osize += osize - 1;
     }
}

void calc(int ntargetsize, int ncursize, int & ncount, int & osize)
{
     osize = ncursize;
     while(ntargetsize >= osize)
     {
         ++ncount;
         osize += osize - 1;
     }
}

bool readInput(list<string> & results) {
    string line;
    ifstream inFile;
    inFile.open ("A-small-attempt3.in", ifstream::in);
    if(inFile.good())
    {
        getline(inFile, line);
        int numberOfTestCases;
        istringstream(line) >> numberOfTestCases;
        for(int i = 0; i < numberOfTestCases; ++i)
        {
                int initsize, motecount;
                getline(inFile, line);
                istringstream strStream(line);
                strStream>>initsize;
                strStream>>motecount;
                std::cout<<"initsize : "<<initsize<<'\n';
                getline(inFile, line);
                istringstream strMotestream(line);
                std::map<int, std::list<int> > motes;
                for(int j = 0; j < motecount; ++j)
                {
                    int motesize;
                    strMotestream >> motesize;
                    motes[motesize].push_back(motesize);

                }
                int cursize = initsize;
                int opSize = 0;

                std::list<int> motelist;
                for(std::map<int, std::list<int> >::iterator it1 = motes.begin(); it1 != motes.end(); ++it1)
                {
                    for(std::list<int>::iterator it = it1->second.begin(); it != it1->second.end(); ++it)
                    {
                                                 motelist.push_back(*it);

                    } 
                }   
                int count = 0;
                for(std::list<int>::iterator it = motelist.begin(); it != motelist.end(); ++it)
                {
                    ++count;
                    std::cout<<(*it)<<' ';
                    if((*it) >= cursize)
                    {
                             //std::cout<<"{ cursize : "<<(*it);
                             int n = motelist.size() - count;
                             //std::cout<<" n : "<<n;
                             int totSize;
                             calc(cursize, n, totSize);
                             //std::cout<<" totSize : "<<totSize;
                             if((*it) >= totSize )
                             {
                                      ++opSize;
                             std::cout<<"{ cursize : "<<cursize;
                             std::cout<<" n : "<<n;
                             std::cout<<" totSize : "<<totSize;
                                      std::cout<<"} ";
                                      //std::cout<<"(*it) >= cursize + cursize - 1"<<'\n';
                                      continue;
                             }

                             calc((*it), cursize, opSize, totSize);
                             //std::cout<<" (*it) : "<<(*it);
                             //std::cout<<" cursize : "<<cursize;
                             //std::cout<<" opSize : "<<opSize;
                             //std::cout<<" totSize : "<<totSize<<"} ";
                             cursize = totSize;
                    }
                    cursize += (*it);
                }     
                std::cout<<'\n';
                std::cout<<"result : "<<opSize<<'\n';
                ostringstream preResultString;
                preResultString<<"Case #"<<i+1<<": "<<opSize;
                
                results.push_back(preResultString.str());
                
        }
        inFile.close();
    }
    else
    {
        cout<<"File couldnt open : "<<endl;
        return false;
    }
    return true;
}

void writeOutput(const list<string> & results)
{
    ofstream outFile("out.txt", ios_base::binary);
    for(list<string>::const_iterator it = results.begin(); it != results.end(); ++it)
    {
        outFile<<(*it)<<'\n';
    }
    outFile.close();
}

int main(int argc, char *argv[])
{
    system("PAUSE");
    list<string> results;
    readInput(results);
    writeOutput(results);
    system("PAUSE");
    return EXIT_SUCCESS;
}
