#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <map>

using namespace std;

bool isc(char c) {
     switch(c)
     {
              case 'a':
              case 'e':
              case 'u':
              case 'i':
              case 'o':
                   return false;
     }
     return true;
}
     
int calc(char * str, int size, int mincsize)
{
     int tsize = 0;
     int csize = 0;
     for(int i = 0; i < size; ++i)
     {
             if(isc(str[i]))
             {
                            ++csize;
                            if(csize == mincsize){
                              tsize = size - i; 
                              break;
                              }
                            
             } else {
                    csize = 0;
                    }
     }
     return tsize;
}

bool readInput(list<string> & results) {
    string line;
    ifstream inFile;
    inFile.open ("A-small-attempt1 (1).in", ifstream::in);
    if(inFile.good())
    {
        getline(inFile, line);
        int numberOfTestCases;
        istringstream(line) >> numberOfTestCases;
        for(int i = 0; i < numberOfTestCases; ++i)
        {
                char str[100];
                int csize = 0;
                getline(inFile, line);
                istringstream strStream(line);
                strStream>>str;
                strStream>>csize;
                int res = 0;
                int strsize = strlen(str);
                for(int j=0; j< strsize; ++j)
                {
                        res += calc(&str[j], strsize - j, csize);
                }
                 
                ostringstream preResultString;
                preResultString<<"Case #"<<i+1<<": "<<res;
                
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
