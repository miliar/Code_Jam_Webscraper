#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

#ifndef FALSE
#define FALSE (0)
#endif

#ifndef TRUE
#define TRUE (1)
#endif
#define _DEBUG_OFF

main() {
    ifstream fin("B-large.in");
	assert( !fin.fail() );
    ofstream fout("B-large.out");
    assert( !fout.fail() );
        
    int T = 0, CaseNum = 0, i = 0, man = 0;
    bool WorkDone = false;
    string Str;

    fin >> T;
    
    while(T--)
    {
        fin >> Str;

#ifndef _DEBUG_OFF
        cout << Str;
#endif
        
        WorkDone = true;        //Assume we got a full happy set :)
        man = 0;
        
        for(i = 0 ; Str[i] ; ++i)
        {
            if(Str[i] == '-')
            {
                WorkDone = false;
                break;
            }
        }
        
        if(!WorkDone)
        {
            do{
                if(Str[0] == '-')
                {
                    ++man;
                    for(i = 0 ; (Str[i] == '-') && (Str[i]) ; ++i)
                    {
                        Str[i] = '+';
                    }
                }
                else
                {
                    ++man;
                    for(i = 0 ; (Str[i] == '+') && (Str[i]) ; ++i)
                    {
                        Str[i] = '-';
                    }
                }
                
                for(i = 0, WorkDone = true ; Str[i] ; ++i)
                {
                    if(Str[i] == '-')
                    {
                        WorkDone = false;
                        break;
                    }
                }
                
                
#ifndef _DEBUG_OFF
                cout << man << " " << Str << "\t";
                if(man > 100)
                {
                    break;
                }
#endif
            }while(!WorkDone);
        }
        
        ++CaseNum;
        

#ifdef _DEBUG_OFF
        fout << "Case #" << CaseNum << ": " << man << endl;
#else
        cout << "Case #" << CaseNum << ": " << man << endl;
#endif
    }
    
    fin.close();
    fout.close();
    
    return 0;
}