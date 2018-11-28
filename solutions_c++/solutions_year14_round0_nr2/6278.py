#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<set>
#include<stack>
#include<vector>
#include<map>
using namespace std;
#define MOD 1000000007
#define MAX 100
int main(){
	  int t;
		double c,f,x;
		int v=0;
		cin >> t;
		while(t--){
		   v++;
			 cin >> c >> f >> x;
			 double cookie=2;
			 double th = (f*(x-c))/c,time=0;
			 while(th > cookie){
			      time+=(c/cookie);
						cookie+=f;
			 }
			 time+=(x/cookie);
       printf("Case #%d: %.7f\n",v,time);
		}
    return 0;
}
