//============================================================================
// Name        : codeforces.cpp
// Author      : xiao chang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
  int t,i,l;
  double c,f,x,time,f0; //c:=cookie to buy farm f:=cookie add x:=goal
  cin>>t;
  l=t;
  while(t--)
  {
	  f0=2;
	  time=0;
     cin>>c;
     cin>>f;
     cin>>x;
     time+=c/f0;
     while((x-c)/f0>=x/(f0+f))
     {
    	 f0+=f;
    	 time+=c/f0;
     }
     time+=(x-c)/f0;
     cout<<"Case #"<<l-t<<": ";
     printf("%.7lf\n",time);

  }
  return 0;

}
