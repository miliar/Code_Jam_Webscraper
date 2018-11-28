#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
//---------- macros ----------
#define fp(i,a,b) for(int i=a; i<b; i++)
#define fm(i,a,b) for(int i=a; i>b; i--)
#define xwon "X won"
#define owon "O won"
#define draw "Draw"
#define incomplete "Game has not completed"
using namespace std;
string maxStr = "102";
map <string, bool> palStrs;
int t, n, m;  long D; int _case;
int lawn[100][100];
bool valid;
int low, h, boundaryH;
int lx,ly;
string currstr;
int currlen;


bool isBiggerThan(string str1, string str2){
	if(str1.length() > str2.length()) return true;
	if(str1.length() < str2.length()) return false;
	return str1.compare(str2) > 0;
}

bool isPal(int index){
	currlen = currstr.length();
	return index>currlen/2 || (currstr[index] == currstr[currlen-index-1] && isPal(index+1));
}

string addString(string bigStr, string smallStr){
	int sum=0, carry=0, biglen = bigStr.length(), smallLen= smallStr.length();
	string retStr = bigStr, vts ="1";
	for(int k=0; k<biglen; k++){
		sum = bigStr[biglen-k-1] - '0';
		if(k<smallStr.length()){
			sum = sum + smallStr[smallLen-k-1] - '0';
		}
		sum = (sum+carry);
		carry = sum/10;
		retStr[biglen-k-1] = sum%10 + '0';
	}
	if(carry){
		vts[0] =  carry + '0';
		retStr = vts + retStr;
	}
	return retStr;
}


string getSquare(string str){
	int carry =0;
	int a,b;
	string newStr= str,  tempStr = "", vts = "1", zstr = "0";
	for(int i=str.length()-1; i>=0; i--){
		newStr[i] = '0';
	}
	for(int i=str.length()-1; i>=0; i--){
		if(str[i] == '0') continue;
		a = str[i] - '0';
		tempStr = str;
		carry = 0;
		for(int k=str.length()-1; k>=0; k--){
			b = str[k] - '0';
			tempStr[k] =(a*b + carry)%10 + '0';
			carry = (a*b + carry)/10;
		}
		if(carry){
			vts[0] =  carry + '0';
			tempStr = vts + tempStr;
		}
		for(int k=0;k<str.length()-1 - i; k++){
			tempStr =  tempStr + zstr;
		}
		newStr = addString(tempStr, newStr);
	}
	return newStr;
}



int main()
{
    _case=1;	
	string str = "0";
	string sqStr = "";
	string lstr, ustr;
	long tot;
	while(1){
		str = addString(str,"1");
		currstr = str;
		if(isPal(0)){
			sqStr = getSquare(str);
			currstr = sqStr;
			if(isPal(0)){
				palStrs[currstr] = true;
			}
		}
		if(isBiggerThan(str,maxStr)) break;
	}
     //cout << "checked max for "  << str << endl;		
    cin >> t;
    while(_case<=t)
    {
		tot = 0;
		cin >> lstr >> ustr;
		while(1){
			if(palStrs[lstr]){
				tot++;
			//	cout << lstr << endl;
            }
            lstr = addString(lstr,"1");
			if(isBiggerThan(lstr,ustr)) break;
			
		}
        cout <<"Case #"<< _case <<": ";
	    cout << tot << endl;
        _case++;
    }
	return 0;
}
