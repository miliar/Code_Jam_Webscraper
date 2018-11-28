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
#define TRUE 1
#define FALSE 0
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
	vector<pair<int,int>> lst;
	int 	total = 0;

/*
********************************************************************************
* Local Macros Definitions
********************************************************************************
*/

#define PRINT(n,x) 		cout << "Case #" << n << ": " << x;
#define PRINT_ITEM(x) 	cout << " " << x;
#define PRINT_CASE(n) 	cout << "Case #" << n << ": ";
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

/*Vector Macro*/
#define fi          	first
#define se          	second
#define all(x)      	(x).begin(), (x).end()


/*
********************************************************************************
* Local Function 
********************************************************************************
*/
int opr_isAllEmpty(){
	F(i, 0, (int)lst.size()){
		if(lst[i].se > 0){
			return FALSE;
		}
	}
	return TRUE;
}
int opr_isAllSame(){
	int num = 0;
	num = lst[0].se;
	F(i, 0, (int)lst.size()){
		if(lst[i].se != num){
			return FALSE;
		}
	}
	return TRUE;
}
int opr_SameCount(){
	int num = 0;
	int count = 0;
	vector<pair<int,int>> lsttemp;
		lsttemp = lst;
			sort(all(lsttemp), [=](pair<int, int> x, pair<int, int> y){return (x.se > y.se);});
	num = lsttemp[0].se;
	F(i, 0, (int)lsttemp.size()){
		if(lsttemp[i].se == num){
			++count;
		}
		else if(lsttemp[i].se < num && lsttemp[i].se >0){
			count = 0;
			break;

			}
	}
	return count;
}

void opr_notsamefunc(){
	vector<pair<int,int>> lsttemp;
	int ctr = 0;
	char ch = 0;
	F(i, 0, (int)lst.size()){
		lsttemp = lst;
		ctr = total;
		lsttemp[i].se -= 1;
		ch = (char) 'A' + lsttemp[i].fi;
		ctr -= 1;
		sort(all(lsttemp), [=](pair<int, int> x, pair<int, int> y){return (x.se > y.se);});
		if(lsttemp[0].se <= (int)(ctr/2)){
			cout<<(ch);
			lst = lsttemp;
			
					cout << " ";
			break;
		}
	}
}

void opr_sameAllfunc(){
	vector<pair<int,int>> lsttemp;
	int ctr = 0;
	char ch = 0;
	F(i, 0, (int)lst.size()){
		if(lst[i].se != 0){
			lsttemp = lst;
			ctr = total;
			lsttemp[i].se -= 1;
			ch = (char) 'A' + lsttemp[i].fi;
			ctr -= 1;
			if(lsttemp[0].se <= (int)(ctr/2)){
				cout<<(ch);
				lst = lsttemp;
				
					cout << " ";
				break;
			}
		}
	}
}
void opr_same2func(){
	vector<pair<int,int>> lsttemp;
	int ctr = 0;
	char ch = 0;
	int prntTimes = 0;
	F(i, 0, (int)lst.size()){
		if(lst[i].se != 0){
			lsttemp = lst;
			ctr = total;
			lsttemp[i].se -= 1;
			ch = (char) 'A' + lsttemp[i].fi;
			ctr -= 1;
			if(lsttemp[0].se <= (int)(ctr/2)){
				cout<<(ch);
				++prntTimes;
				lst = lsttemp;
				if(prntTimes == 2){
					
					cout << " ";
					break;
					}
			}
		}
	}
}


/*
********************************************************************************
* Main Function
********************************************************************************
*/

int main(void){
    int     nTestCases = 0;
	int 	count = 0;
	int 	temp = 0;
	int 	sts = FALSE;
	
#ifdef FILE_OUTPUT
    FILE*   fpIn = freopen("A-large.in", "r+", stdin);
    FILE*   fpOut = freopen("out-large", "w+", stdout);
#endif

    cin >> nTestCases;
    //cin.ignore(1, '\n'); 
    F(z, 0, nTestCases){
    	cin>>count;
		lst.clear();
		sts = FALSE;
		total = 0;
		F(i, 0, count){
			cin>>temp;
    		lst.push_back(make_pair(i, temp));
			total += temp;
			//TRACE1(total);
		}
		PRINT_CASE((z+1));
		while(opr_isAllEmpty()==FALSE){
			if(opr_isAllSame() != TRUE && sts != TRUE){
			sort(all(lst), [=](pair<int, int> x, pair<int, int> y){return (x.se > y.se);});
				opr_notsamefunc();
			}
			else{
				sts = TRUE;
				if(opr_SameCount() == 2){
					opr_same2func();
				}
				else{
					opr_sameAllfunc();
				}
			}
		}
		//for_each(all(lsttemp), [=](const pair<int,int> x){cout << x.fi << "->" << x.se << " ";});
		cout<<endl;
    }

#ifdef FILE_OUTPUT
    fclose(fpIn);
    fclose(fpOut);
#endif
    
    return 0;
}

