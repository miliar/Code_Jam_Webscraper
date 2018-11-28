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
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	//ios::sync_with_stdio(false);
	FILE *fin = freopen("A-small-attempt5.in", "r", stdin);
	//assert( fin!=NULL );
	FILE *fout = freopen("A-small-attempt5.out", "w", stdout);
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    if (n==0){
		cout << "Case #" << i << ": INSOMNIA" << endl;
	}
	else{
		int dataset=1000000;
		int ch[10];
		for (int j=0; j<=9; j++){
			ch[j]=0;
		}
		int flag=0;
		int x=n;
		for (x=n;((x<=dataset)&&(flag==0)); x=x+n){
			int x1=x;
			while (x1>0){
				int k=x1%10;
				x1=x1/10;
				ch[k]=1;
				//cout<<x1<<endl;
				
			}
				flag=0;
				int flag1=0;

				for (int l=0; l<=9;l++){
					if (ch[l]==0){
						flag1=1;
					}
				if (flag1==1){
					flag=0;
				}
				else{
					flag=1;
				}

			}

		}
		if (flag==0){
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else{
			cout << "Case #" << i << ": " <<x-n<< endl;
		}
		
	}
	
	
	
	
	
	
	
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}
