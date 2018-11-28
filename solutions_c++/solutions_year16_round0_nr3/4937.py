// Google1.cpp: определяет точку входа для консольного приложения.
//
//#include <bits/stdc++.h>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
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
	FILE *fin = freopen("C-small-attempt7.in", "r", stdin);
	//assert( fin!=NULL );
	FILE *fout = freopen("C-small-attempt7.out", "w", stdout);
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": " <<endl;
	  cin >> n>>m;  // read n and then m.
	
	  int *a=new int [n];
		a[0]=1;
		a[n-1]=1;
		for (int j=1; j<n-1;j++){
			a[j]=0;
		}
		int flag=0;
		int i1=0;
		while ((i1<m)){
			a[1]=a[1]+1;
			//cout<<"1"<<endl;
			for (int j=1; j<=n-2;j++){
				if (a[j]==2) {
					a[j]=0;
					a[j+1]=a[j+1]+1;
				}
			}
			if (a[n-1]==2) {
				a[n-1]=1;
				flag=1;
			}
			else{
				_int64 *s=new _int64[11];
				int flag=0;
				_int64 b=1;
				for (int j=2;((j<=10)&&(flag==0));j++){
					b=1;
					for (int k=1; k<n; k++){
						b=b+a[k]*MyPow(j,k);
						
					}
					//cout<<j<<" "<<b<<endl;
					s[j]=IsPrime(b);
					if (s[j]==0){
						flag=1;
					}
				}
			//	for(int j=n-1;j>=0;j--){
			//			cout<<a[j];
			//	}
			//	cout<<endl;
				if (flag==0){
					i1=i1+1;
					for(int j=n-1;j>=0;j--){
						cout<<a[j];
					}
					
					for (int j=2;j<=10;j++){
					cout<<" "<<s[j];
					}
					cout<<endl;
				}

			}
		}
			
		
  
	}
	
	
}	