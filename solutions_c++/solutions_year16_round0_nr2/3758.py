/*
 * testthing.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: rss
 */
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int T; string str;
int main() {
	cin>>T;
	for (int i=1; i<=T; i++) {
		cin>>str;
		str.append("+");
		int f=0;
		for (int j=1; j<str.length(); j++) {
			f+=str[j]!=str[j-1];
		}
		printf("Case #%d: %d", i, f);
	}
}
