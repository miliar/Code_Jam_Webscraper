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
    ifstream fin("A-large.in");
	assert( !fin.fail() );
    ofstream fout("A-large.out");
    assert( !fout.fail() );
//    ofstream fout1("B-small-1.out");
//    assert( !fout1.fail() );
        
    int T = 0, CaseNum = 0, index = 0, modRes = 0, seenDigitCnt = 0;
    long long int res = 0, N = 0, multiplier = 0; 
    bool seenDigit[10] = {0}, seenAll = FALSE;
    
    fin >> T;
    
    while(T--)
    {
        fin >> N;
        
        multiplier = 1;
        res = N * multiplier;
        
        if(N)
        {
            seenDigitCnt = 0, seenAll = FALSE;
            while((res >= N) && (!seenAll))
            {
#ifndef _DEBUG_OFF
                cout << res << " "; 
#endif
                while(res)
                {
                    modRes = res % 10;
#ifndef _DEBUG_OFF
                    cout << modRes << seenDigit[modRes];
#endif
                    
                    if(!seenDigit[modRes])
                    {
                        seenDigit[modRes] = true;
                        ++seenDigitCnt;
#ifndef _DEBUG_OFF
                        cout << " " << seenDigitCnt << seenDigit[modRes] << " ";
#endif
                        if(seenDigitCnt >= 10)
                        {
                            seenAll = true;
                            break;
                        }
                    }
                    
                    res /= 10;
                }
                
#ifndef _DEBUG_OFF
                for(index = 0 ; index < 10 ; ++index)
                {
                    cout << seenDigit[index];
                }
                cout << endl;
#endif

                if(!seenAll)
                {
                    ++multiplier;
                    res = N * multiplier;
                }
            }
        }
        
        for(index = 0 ; index < 10 ; ++index)
        {
            seenDigit[index] = false;
        }
        ++CaseNum;
        
#ifdef _DEBUG_OFF
        fout << "Case #" << CaseNum << ": ";
#else
        cout << "Case #" << CaseNum << ": ";
#endif

        if(seenAll)
        {
#ifdef _DEBUG_OFF
            fout << (N * multiplier);
#else
            cout << (N * multiplier);
#endif
        }
        else
        {
#ifdef _DEBUG_OFF
            fout << "INSOMNIA";
#else
            cout << "INSOMNIA";
#endif
        }
        
#ifdef _DEBUG_OFF
        fout << endl;
#else
        cout << endl;
#endif
    }
    
    return 0;
}