#include <stdio.h>
#include <cstdlib>
#include <string.h>

using namespace std;

int getValueFromString(const char *str, int nVal);
int totalFromSubstring(const char *str, int strLength, int nVal);

int main()
{
    int totalCases;
    int nCases;
    scanf("%d", &nCases);
    totalCases = nCases;
    
    while ( nCases-- )
    {
        // Setup stuff
        char buffer[512];
        scanf("%s", buffer);
        int nValue;
        scanf("%d", &nValue);
        
        int value = getValueFromString( buffer, nValue );
        
        printf( "Case #%d: %d\n", totalCases - nCases, value );
    }
    return 0;
}

int totalFromSubstring(const char *str, int strLength, int nVal){
    int total = 0, i = 0, consec = 0;
    char ch;
	while( i < strLength ){
        ch = str[i];
		if( !( ch=='a'|| ch=='e'|| ch=='i'|| ch=='o'|| ch=='u') )
            ++consec;
        else
            consec = 0;
        
        if ( consec == nVal ){
            ++total;
            total += totalFromSubstring( &str[1], strLength - 1, nVal );
            break;
        }
        ++i;
	}
    return total;
}

int getValueFromString(const char *str, int nVal){
    unsigned long strLength = strlen( str );
    int total = totalFromSubstring( str, (int)strLength, nVal );
    while ( strLength >= nVal ){
        char substring[ strLength ];
        strncpy( substring, str, strLength );
        substring[ strLength - 1 ] = '\0';
        --strLength;
        total += totalFromSubstring( substring, (int) strLength, nVal );
    }
    
	return total;
}