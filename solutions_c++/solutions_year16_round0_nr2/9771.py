//
//  Revenge of the Pancakes.cpp
//  CodeJam
//
//  Created by Yen Feng Cheng on 4/9/16.
//  Copyright © 2016 Yen-Feng Cheng. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include<algorithm>
#include <queue>

using namespace std;
map<string, int> flipNumber;

string flipStr(string str) {
	for ( string::iterator it = str.begin(); it != str.end(); it++ ) {
		if ( (*it)=='+' ) (*it) = '-';
		else (*it) = '+';
	}
	return str;
}

bool isAllPlus(string str) {
	for ( string::iterator it = str.begin(); it != str.end(); it++ ) {
		if ( (*it)=='-' ) return false;
	}
	return true;
}

int computeAns(string str, int times) {
	if ( isAllPlus(str) ) {
		return times;
	} else if ( flipNumber.count(str)>0 && flipNumber[str]==INT_MAX){	//已經在搜尋途中
		return INT_MAX;	//不算數，直接return, 會有其他更短路徑回傳answer
	} else if ( flipNumber.count(str)>0 && flipNumber[str]>=0 ){	//找到cache, + times
		return flipNumber[str]+times;
	} else {
		int tmpAns;
		flipNumber[str]=INT_MAX;	//still searching for answer
		for ( int i=1; i<=str.length(); i++ ) {
			string strTmp = flipStr(str.substr(0,i));
			reverse(strTmp.begin(), strTmp.end());
			tmpAns = computeAns( strTmp+str.substr(i), times+1 );
			if ( tmpAns < flipNumber[str] ) flipNumber[str] = tmpAns;
		}
		return flipNumber[str];
	}
}

int computeAnsBFS(string str) {
	int times=0, layer=0;
	queue<string> strQue;
	flipNumber[str]=layer;
	if ( isAllPlus(str) ) return flipNumber[str];
	while ( true ) {
		for ( int i=1; i<=str.length(); i++ ) {
			string strTmp = flipStr(str.substr(0,i));
			reverse(strTmp.begin(), strTmp.end());
			strTmp = strTmp + str.substr(i);
			if ( isAllPlus(strTmp) ) return flipNumber[str]+1;
			if ( flipNumber.count(strTmp)==0 ) {	//已經有的話就不放進去，一定不是最佳路徑
				flipNumber[strTmp] = flipNumber[str]+1;
				strQue.push(strTmp);
			}
		}
		//layer++;
		str = strQue.front();
		strQue.pop();
	}
	
	//return times;
}

int computeAnsFast(string str) {
	int ans;
	if ( isAllPlus(str) ) return 0;
	int numPlus=0;
	string strMod;
	int flag=-1;
	for (string::iterator it = str.begin(); it!=str.end(); it++) {
		if ( (*it)=='+' && flag!=1 ) {
			numPlus++;
			flag=1;
		} else if ( (*it)=='-' ) {
			flag=0;
		}
	}
	ans = numPlus*2+1;
	if ( str.back()=='+' && numPlus!=0 ) ans-=2;
	if ( str.front()=='+' ) ans-=1;
	return ans;
}

int main() {
	int T;
	string str;
	cin>>T;
	getchar();
	for ( int i=0; i<T; i++ ) {
		getline(cin, str);
		flipNumber.clear();
		cout<<"Case #"<<i+1<<": "<<computeAnsFast(str)<<endl;
	}
}