#include <string.h>
#include <stdio.h>
#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

bool check(int *A, int n)
 {
  char s[20];
  int t;

  sprintf(s,"%d",n); t = 0;
  for(int k=0;k<strlen(s);k++) A[s[k]-'0'] = 1;
  for(int k=0;k<10;k++) t += A[k];
  //cout << t << " " << n << endl;
  if(t==10) return true;
  return false;
 }

int main()
 {
  int t,n,c,f;
  int A[10];
  cin >> t;
  for(int i = 0; i < t; i++)
   {
	cin >> n;
	for(int k=0;k<10;k++) A[k] = 0; c = 1; f = 0;
	while(f==0)
	 {
	  if(check(A,n*c)) f=2;
	  c++; if(n == n*c) f = 1;
     }
     if(f==1) cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
     else     cout << "Case #" << i+1 << ": " << n*(c-1)    << endl;
   }
  return 0;
 }
