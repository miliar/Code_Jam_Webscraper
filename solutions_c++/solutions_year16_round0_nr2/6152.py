// Google1.cpp: определяет точку входа для консольного приложения.
//
//#include <bits/stdc++.h>


#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include "StdAfx.h"
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
unsigned long int IsPrime(unsigned long int a)
{
	for (unsigned long int i=2; i<a;i++){
		unsigned long int b=a%i;
		if (b==0){
			return i;
		}
	}
	return 0;
}
unsigned long int MyPow(int a,int b)
{
	unsigned long int s=1;
	for(int i=1; i<=b;i++){
		s=s*a;
	}
	return s;
}
class m
{
public:
    m(char * p)
    {
        x = p;
    }
    char * x;
};
bool operator==(char* x, const m& y)
{
    int size1 = strlen(x);
    int size2 = strlen(y.x);
    if(size1 != size2) return false;
 
    for(int i =0; i < size1; i++)
    {
        if(x[i] != y.x[i]) return false;
    }
    return true;
}

void main() {
	//ios::sync_with_stdio(false);
	FILE *fin = freopen("B-large.in", "r", stdin);
	//assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
	  int c=0;
		char s[100];
		
	  cin >> s;  
		int flag=0;
		int l=strlen(s);
	  while (flag==0){
		  //for(int i1=0;i1<=l;i1++)
		//	  cout<<s[i1];
		  //cout<<endl;
		  flag=1;
		  for (int j=0; j<=l; j++){
			  
			 // cout<<s[j];
			  if (s[j]=='-'){
				  //cout<<j;
				  flag=0;
			  }

		  }
		  //cout<<flag;
		  if (flag==0){

			  int last=l-1;
			  for (last=l-1;((last>=0)&&(s[last]=='+'));last--){
					
			  }
			  //cout<<last;
			  c=c+1;
			  //for (int i1  = 0; i1 <=last / 2; i1++){
			//	swap(s[i1], s[last - i1 - 1]);
			 // }
			  for (int i1=0; i1<=last;i1++){
				  if (s[i1]=='+'){
					  s[i1]='-';
				  }
				  else{
					  s[i1]='+';
				  }
			  }

		  }
	  }
			
		
		cout << "Case #" << i << ": " <<c<<endl;
	}
	
	
	
	
	
	//int ma;
	//cin>>ma;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
 }

