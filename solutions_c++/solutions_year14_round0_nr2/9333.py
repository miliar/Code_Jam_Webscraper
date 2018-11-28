#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
#include <sstream>
#include <string>

using namespace std;

#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mp make_pair
#define pb push_back
#define sz size()
#define F first
#define S second
#define FO(i,x) for(int i=0;i<x;i++)

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
//  int dx[]={-2,-2,-1,-1,1,1,2,2}; int dy[]={-1,1,-2,2,-2,2,-1,1}; // Knight Dir
//  int dx[]={-1,-1,-1,0,1,1,1,0}; int dy[]={-1,0,1,1,1,0,-1,-1};  // 8 Dir
//  int dx[]={0,1,-1,0}; int dy[]={1,0,0,-1}; // 4 Dir
double C,F,X;
double get(double pls){
	   double t1=X/pls;
	   double t2=C/pls;
	   t2+=(X/(pls+F));
	   if(t1<t2) return t1;
	   return get(pls+F)+C/pls;
}
int main(){
     READ("B-small-attempt0.in");
     WRITE("B-small-attempt0.out");
     int t,a=1;
     cin>>t;
     while(t--){
     	 double pls=2.0,have=0;
         double res=0;
		 cin>>C>>F>>X;
     	 printf("Case #%d: %.7F\n",a++,get(2));
     }
	 return 0;
}
