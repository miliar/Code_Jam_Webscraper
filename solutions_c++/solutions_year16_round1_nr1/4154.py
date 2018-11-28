// Google1.cpp: определяет точку входа для консольного приложения.
//
//#include <bits/stdc++.h>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <string.h> 
#include "StdAfx.h"
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <math.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
_int64 IsPrime(_int64 a)
{
	_int64 fl=0;

	for (_int64 i=5; ((i<pow(a,0.5))&&(fl==0));i=i+2){
		_int64 b=a%i;
		if (b==0){
			return i;
			fl=1;
		}
		//cout<<"IsPrime"<<b<<endl;
	}
	if (fl==0){
		return 0;
	}
}
_int64 MyPow(int a,int b)
{
	_int64 s=1;
	for(int i=1; i<=b;i++){
		s=s*a;
	}
	return s;
}
void main() {
	//ios::sync_with_stdio(false);
	FILE *fin = freopen("A-large.in", "r", stdin);
	//assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
		
	  
		//string  s1; 
		string s; 
		cin>>s;
		string(s1);
	char alp[]="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	int alpl=strlen(alp);
	int l=s.length();
	
	for (int i=0;i<l;i++){
		string a,a1;

		a=s[i];
		int l1=s1.length();
		if (l1==0){
			s1+=a;
		}
		else{
			a1=s1[0];
			int ai=0;
			int a1i=0;
			for (int j=0;j<alpl;j++){
				if (alp[j]==a[0]){
					ai=j;
				}
				if (alp[j]==a1[0]){
					a1i=j;
				}
			}
			if (a1i<=ai){
				s1=a+s1;
				//cout<<a1<<a1i<<" "<<a<<ai<<endl;
			}
			else
			{
				s1=s1+a;
				//cout<<a1<<a1i<<" "<<a<<ai<<endl;
			}
			
		}
		
		
	}
	cout << "Case #" << i << ": " <<s1<<endl;
	}
}
			
		
  