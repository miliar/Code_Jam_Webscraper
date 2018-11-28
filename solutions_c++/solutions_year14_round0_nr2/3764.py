#include<cstdio>
#include <cctype>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include <deque>
#include <math.h>
#include<stdio.h>
#include<memory.h>
using namespace std;


typedef stringstream ss;
typedef vector<string> vs;
typedef vector<int> vi;
typedef unsigned long long int64;

#define PI 3.14159265
#define pb push_back
#define sz size()
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define fornm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble(

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000
int main()
{
//	freopen("B-small-attempt0.in", "r", stdin);	freopen("respuestaB_S.out", "w+", stdout);

	freopen("B-large.in", "r", stdin);	freopen("respuestaB_L.out", "w+", stdout);

	
    int T,cont;
    cin>>T;
	double C,F,X, t=0.0,speed=2.0;
	string sC,sF,sX;
	
    fornm(tc,1,T)
    {
	       cin >> sC >> sF >> sX;
		   t=0.0;
		   double t2 = 0.0;
		   speed= 2.0;
		   C = toDouble(sC);
		   F = toDouble(sF);
		   X = toDouble(sX);
		   int cont = 0;
		   double ant = X/speed;
		   while(ant >= X/speed+t2)
		   { 
		   ant = X/speed+t2;
		      t = C/speed;
			  t2 += C/speed;
			  speed += F;
			//  cout<<ant<<" - " <<t<<"  -  "<<speed<<" - "<<X/speed+t2 <<endl;
			  
		   }
 		   cout<<"Case #"<<tc<<": ";
		   printf( "%.7f\n",ant);
		   
	}
	return 0;
}

