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
#include <vector>
#include <deque>
#include <algorithm>
#include <iterator>


using namespace std;

/*
********************************************************************************
* Local Macros
********************************************************************************
*/

#define CODE_RELEASE_ENABLED

#ifndef CODE_RELEASE_ENABLED
	#define FILE_OUTPUT
	//#define	TRACE_ENABLE
#endif

#define MAX_STR_CNT	10

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
const string strArr[] = { "TWO", "ZERO", "SIX", "EIGHT", "SEVEN", "FIVE", "FOUR", "THREE", "ONE", "NINE"};
const int inArr[] = {2, 0, 6, 8, 7, 5, 4, 3, 1, 9};
vector<int> ans;

/*
********************************************************************************
* Local Macros Definitions
********************************************************************************
*/

#define PRINT(n,x) 		cout << "Case #" << n << ": " << x;
#define PRINT_ITEM(x) 	cout << " " << x;
#define PRINT_CASE(n) 	cout << "Case #" << n << ":";
#define PRINT_NEWLINE()	cout << endl;

#define F(i,s,n)  		for(unsigned int i=s;i<(n);i++)
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

/*Vector Macro*/
#define fi          	first
#define se          	second
#define all(x)      	(x).begin(), (x).end()


/*
********************************************************************************
* Local Function Prototype
********************************************************************************
*/
string checkWord(string num);

/*
********************************************************************************
* Main Function
********************************************************************************
*/

int main(void){
    int     	nTestCases = 0;
	string 		temp;
	//vector<int> lst;
	
#ifdef FILE_OUTPUT
    FILE*   fpIn = freopen("A-large.in", "r+", stdin);
    FILE*   fpOut = freopen("out-large", "w+", stdout);
#endif
    cin >> nTestCases;

    cin.ignore(1, '\n'); 
    F(i, 0, nTestCases){
    	cin>>temp;

		ans.clear();
		
		while(temp.length() != 0){
			temp = checkWord(temp);
		}
		sort(all(ans));
		PRINT_CASE(i+1);
		cout<<" ";
		for_each(all(ans), [=](const int x){cout<<x;});
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

string checkWord(string num){
	F(i, 0, MAX_STR_CNT){
		int score = 0;
			string s = num;
		F(j, 0, strArr[i].length()){
			F(k, 0, s.length()){
				if(s[k] == strArr[i][j]){
						//TRACE3(s[k], strArr[i][j], score);
						s[k] = '-';
					++score;
					break;
				}
			}
			if(score == strArr[i].length())
				break;
		}
		if(score == strArr[i].length()){
			
			F(j, 0, strArr[i].length()){
				F(k, 0, num.length()){
					if(num[k] == strArr[i][j]){
						num[k] = '-';
						break;
					}
				}
			}
			ans.push_back(inArr[i]);
			TRACE4(strArr[i], num, score, strArr[i].length());
			break;
		}
	}
	F(k, 0, num.length()){
		if(num[k] == '-'){
			num.erase(k,1);
			k = 0;
		}
	}
	return num;
}

