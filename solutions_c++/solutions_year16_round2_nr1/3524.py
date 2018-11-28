//iejr Header files
#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <cstring>
#include <sstream>
#include <bitset>
#include <cmath>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <limits.h>
#include <ctime>
#include <cctype>
#include <functional>
#include <utility>
#include <numeric>

using namespace std;

//iejr: Type defination
typedef unsigned long long int             ULLN;
typedef long long int                      LLN;
typedef vector<int>                        VI;
typedef vector<vector<int> >               VVI;
typedef vector<string>                     VS;
typedef vector<vector<string> >            VVS;


//iejr: Compile Options
#define C11_Standard
//
#ifdef C11_Standard
    #include <unordered_set>
    #include <unordered_map>

    #define HASHSET                  unordered_set
    #define HASHMAP                  unordered_map;
#endif // C11_Standard


//iejr: Local Debug
#define INPUT_REDIRECTION
#define OUTPUT_REDIRECTION

#define DICTSIZE    26

vector<string> vDict = {
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"
};

string dfs( int *nHash, string &strCur, int nLastNum ){
    int nCnt = DICTSIZE;
    for( int i = 0;i < DICTSIZE;++i ){
        if( nHash[i] == 0 ){
            --nCnt;
        }
    }

    if( nCnt == 0 ){
        return strCur;
    }

    for( int i = nLastNum;i <= 9;++i ){
        int nHashCpy[DICTSIZE];
        for( int j = 0;j < DICTSIZE;++j ){
            nHashCpy[j] = nHash[j];
        }
        bool bIsOK = true;
        for( int j = 0;j < vDict[i].length();++j ){
            nHashCpy[vDict[i][j] - 'A']--;
            if( nHashCpy[vDict[i][j] - 'A'] < 0 ){
                bIsOK = false;
                break;
            }
        }

        if( bIsOK ){
            char c = i + '0';
            string strCurr = strCur + c;
            string strNext = dfs( nHashCpy, strCurr, i );
            if( strNext != "" ){
                return strNext;
            }
        }

    }

    return "";
}

//iejr: Main Function
int main()
{

#ifdef INPUT_REDIRECTION
    freopen( "A-small-attempt0.in", "r", stdin );
#endif // INPUT_REDIRECTION

#ifdef OUTPUT_REDIRECTION
    freopen( "out.txt", "w", stdout );
#endif // OUTPUT_REDIRECTION

    int T = 0;
    scanf( "%d", &T );
    for( int i = 0;i < T;++i ){
        int nHash[DICTSIZE];
        memset( nHash, 0, DICTSIZE * ( sizeof(int) )  );

        char buff[3000];
        memset( buff, 0, 3000 );
        scanf( "%s", buff );

        for( int i = 0;i < strlen( buff );++i ){
            nHash[buff[i] - 'A']++;
        }

        string strStart = "";
        string sNumber = dfs( nHash, strStart, 0 );

        cout<<"Case #"<<(i + 1)<<": "<<sNumber<<endl;
    }

#ifdef INPUT_REDIRECTION
    fclose( stdin );
#endif // INPUT_REDIRECTION

#ifdef OUTPUT_REDIRECTION
    fclose( stdout );
#endif // OUTPUT_REDIRECTION

    return 0;
}
