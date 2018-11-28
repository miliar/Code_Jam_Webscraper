/*
* Author    ->  Aashish Sud
* DOC       ->  9th April, 2016
* UserName  ->  codeDEXTER
* Twitter   ->  @codeDEXTER
* Email     ->  aashishsud1139066@gmail.com
* Website   ->  www.codedexter.com
* Desc      ->  Submission for Google Code Jam 2016
*/

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>


using namespace std;

/*
********************************************************************************
* Local Macros
********************************************************************************
*/

#define CODE_RELEASE_ENABLED

#ifndef CODE_RELEASE_ENABLED
	#define FILE_OUTPUT
	#define	TRACE_ENABLE
#endif

/*
********************************************************************************
* Type Defines
********************************************************************************
*/
typedef unsigned long int uint32;

/*
********************************************************************************
* Global Variables
********************************************************************************
*/
int     nPtr = 0;
int     nPtrStart = 0;
int     nPtrEnd = 0;
char	strIP[1000] = {'\0'};
char	strOP[2000] = {'\0'};
char	chFirstChar = '\0';

int 	nFinalPtr = 0;
char	strFinal[1000] = {'\0'};


/*
********************************************************************************
* Local Macros Definitions
********************************************************************************
*/

#define PRINT(n,x) 		cout << "Case #" << n << ": " << x;
#define PRINT_ITEM(x) 	cout << " " << x;
#define PRINT_CASE(n) 	cout << "Case #" << n << ":";
#define PRINT_NEWLINE()	cout << endl;

#define F(i,s,n)  		for(int i=s;i<(n);i++)
#define FIncl(i,s,n)  	for(int i=s;i<=(n);i++)
#define FRev(i,n,s)  	for(int i=(n)-1;i>=s;i--)
#define FRevIncl(i,n,s) for(int i=(n);i>=s;i--)

#ifdef TRACE_ENABLE
    #define TRACE(x)            cout << x << endl;
    #define TRACE1(x)           cout << __FUNCTION__ << ":" << __LINE__ << ": "#x" = " << x << endl;
    #define TRACE2(x,y)         cout << __FUNCTION__ << ":" << __LINE__ << ": "#x" = " << x << " | "#y" = " << y << endl;
    #define TRACE3(x,y,z)       cout << __FUNCTION__ << ":" << __LINE__ << ": "#x" = " << x << " | "#y" = " << y << " | "#z" = " << z << endl;
    #define TRACE4(a,b,c,d)     cout << __FUNCTION__ << ":" << __LINE__ << ": "#a" = " << a << " | "#b" = " << b << " | "#c" = " << c << " | "#d" = " << d << endl;
    #define TRACE5(a,b,c,d,e)   cout << __FUNCTION__ << ":" << __LINE__ << ": "#a" = " << a << " | "#b" = " << b << " | "#c" = " << c << " | "#d" = " << d << " | "#e" = " << e << endl;
    #define TRACE6(a,b,c,d,e,f) cout << __FUNCTION__ << ":" << __LINE__ << ": "#a" = " << a << " | "#b" = " << b << " | "#c" = " << c << " | "#d" = " << d << " | "#e" = " << e << " | "#f" = " << f << endl;
#else
    #define TRACE(x)
    #define TRACE1(x)
    #define TRACE2(x,y)
    #define TRACE3(x,y,z)
    #define TRACE4(a,b,c,d)
    #define TRACE5(a,b,c,d,e)
    #define TRACE6(a,b,c,d,e,f)
#endif

/*
********************************************************************************
* Local Function Prototype
********************************************************************************
*/


/*
********************************************************************************
* Main Function
********************************************************************************
*/

int main(void){
    int     nTestCases = 0;
    
#ifdef FILE_OUTPUT
    FILE*   fpIn = freopen("A-large.in", "r+", stdin);
    FILE*   fpOut = freopen("out_large", "w+", stdout);
#endif

    cin >> nTestCases;
    cin.ignore(1, '\n'); 
    F(i, 0, nTestCases){
    	gets(strIP);
		nPtr = 0;
		nPtrStart = (2000/2);
		nPtrEnd = (2000/2);
		chFirstChar = strIP[0];
		strOP[nPtrStart] = chFirstChar;
		++nPtr;
		
		while(strIP[nPtr] != '\n' && strIP[nPtr] != '\r' && strIP[nPtr] != '\0'){
			if(strIP[nPtr] >= strOP[nPtrStart]){
				strOP[--nPtrStart] = strIP[nPtr];
			}
			else{
				strOP[++nPtrEnd] = strIP[nPtr];
			}
			++nPtr;
		}

		nFinalPtr = 0;
		
		FIncl(j,nPtrStart,nPtrEnd){
			strFinal[nFinalPtr] = strOP[j];
			++nFinalPtr;
		}
		strFinal[nFinalPtr] = '\0';

		
		PRINT((i+1), strFinal);
		PRINT_NEWLINE();
    }

    
#ifdef FILE_OUTPUT
    fclose(fpIn);
    fclose(fpOut);
#endif
    
    return 0;
}

/*
********************************************************************************
* Local Function
********************************************************************************
*/


