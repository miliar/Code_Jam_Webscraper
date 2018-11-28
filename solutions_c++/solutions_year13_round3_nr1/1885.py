#include <algorithm>  
#include <iostream>  
#include <iomanip>  
#include <fstream>  
#include <sstream>  
#include <string>  
#include <list>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
using namespace std;  

#define FOR(i,a,b) for(long i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  

int main(int argc, char** argv)
{
    ifstream in;
    in.open(argv[1],ios::in);
    ofstream out;
    out.open(argv[2],ios::out);
    int N = 0;
    in>>N;
    cout << " Total  " << N <<endl;
    REP(caseN,N)
    {
        cout<<"solving case "<<caseN+1<<endl;
        string str;
        long n;
        
        in >> str >> n;

        char* inString = strdup(str.c_str());
        size_t inLen = strlen(inString);
        
        long total = 0;
        for(ulong i = 0; i < (inLen - n +1); ++i)
        {
            for(ulong j = i + (n-1); j < inLen; ++j)
            {
            //cout << "iter i = " << i << " j = " << j << endl; 
                long consC = 0;
                bool breakLoop = false;
                char* start = inString +i ;
                char* end = inString+j;
                while(start <= end)
                {
                    switch(*start)
                    {
                        case 'a':
                        case 'e':
                        case 'i':
                        case 'o':
                        case 'u':
                            consC = 0;
                            break;
                        default:
                            consC++;
                            //cout << " const count becomes " << consC<< " for " << (*start) << endl;
                             
                            if(consC == n)
                            {
                                //cout <<"\t ADDING (total = " << total << " inlen = " << inLen << " j = " << j<<endl;
                                total += (inLen - j ); //check
                                breakLoop = true;
                                break;
                            }
                    }
                    ++start;
                    if(breakLoop) break;
                }
                if(breakLoop)break;
            }
            //cout << "        total = " << total<<endl;
        }
        free(inString);

        out << "Case #"<<caseN+1<<": " << total << endl;

    }
        
    in.close();
    out.close();
    return 0;
}
