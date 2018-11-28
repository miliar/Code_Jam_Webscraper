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
#define CPS 2

string voltea(string str)
{
	int l = str.size();
	string res = "";
	//for(int i = l-1;i>-1; i--)
	for(int i = 0;i<l;i++)
	{
		if(str.substr(i,1)=="-")
			res+="+";
			else
			res +="-";
	}
	return res;
}
string quitaMas(string str)
{
	int  l = str.size();
	string res = "";
	int  i = l-1;
	for(i;i>-1; i--)
	   if(str.substr(i,1)=="-")break;
	return str.substr(0,i+1);
}

bool listo(string str)
{
	int  l = str.size();
	for(int i=l-1;i>-1; i--)
	   if(str.substr(i,1)=="-")return false;
	return true;
}
int main()
{
//	freopen("B-small-attempt0.in", "r", stdin);	freopen("respuestaB_S.out", "w+", stdout);

	freopen("B-large.in", "r", stdin);	freopen("respuestaB_L.out", "w+", stdout);

	
    int T,cont;
    cin>>T;
	string s;
	
    fornm(tc,1,T)
    {
	       cin >> s;
	       int cont = 0;
	       while(!listo(s))
	       {
	       		s = quitaMas(s);
	       	//	cout<<s<<"       :         ";
			   	s = voltea(s);  
			 //  	cout<<s<<endl;
			   	cont ++ ;
		   }
		   cout<<"Case #"<<tc<<": "<<cont<<endl;
		   
	}
	return 0;
}

