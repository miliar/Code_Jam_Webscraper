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
typedef long long int64;

#define PI 3.14159265
#define pb push_back
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define fornm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//NOTES:lowbit(
int dx[]={1,1,0},dy[]={0,1,1};
#define MAXIMO 10000

struct Dep
{
   pair<pair<string, string>, int>  Ini;     
};
// Creamos su función de comparación
int Cmp( const void *Uno, const void *Otro )
{ Dep *UnoP  = (Dep *)Uno;
  Dep *OtroP = (Dep *)Otro;

if((UnoP->Ini).second != (OtroP->Ini).second)
  return (UnoP->Ini).second - (OtroP->Ini).second;
if( ((UnoP->Ini).first).first != ((OtroP->Ini).first).first) 
     return ((UnoP->Ini).first).first .compare( ((OtroP->Ini).first).first);
return ((UnoP->Ini).first).second .compare( ((OtroP->Ini).first).second); 
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin); 	freopen("respuestaB_S.out", "w+", stdout);
//	freopen("B-large-practice.in", "r", stdin);  	freopen("respuestaB_L.out", "w+", stdout);


    int T;
	string sC,sJ;
	cin>>T;
    char buffer [1];
    fornm(tc,1,T)
    {
	   cin >> sC >> sJ;
	   int  l  = sC.length();
	   int posi = 0 ;
	   vi vpC, vpJ;
	   forn(i,l){
	   if(sC[i] == '?')vpC.pb(i);
	   if(sJ[i] == '?') vpJ.pb(i); 
	}
	
	  posi  = vpC.size();
	   int curC = 0 ;
	   int curJ = 0;
	   vs posC;
	   posC.pb(sC);
	   forn(i,vpC.size())
	   {
	   	vs tempC;
	   	forn(kk,posC.size())
	   	{
	    	forn(k,10)
		   	{
		   	  posC[kk][vpC[i]]= '0' + k;
		   	    tempC.pb(posC[kk]);
		     }
		    
	    }
	    posC = tempC;  
	   }
	   vs posJ;
	   posJ.pb(sJ);
	   forn(i,vpJ.size())
	   {
	   	vs tempJ;
	   	forn(kk,posJ.size())
	   	{
	    	forn(k,10)
		   	{
		   	  posJ[kk][vpJ[i]]= '0' + k;
		   	    tempJ.pb(posJ[kk]);
		     }
		    
	    }
	    posJ = tempJ;  
	   }
	   
	   
	   vector<pair<pair<string, string>, int> > resT ;
	   forn(kc,posC.size())
	   forn(kj,posJ.size())
	   {
	   	int dif = abs( atoi( posC[kc].c_str()) - atoi(posJ[kj].c_str()));
	   	resT.pb(make_pair(make_pair(posC[kc],posJ[kj]),dif));
	   }
	   
	   qsort( (void *)&resT[0], resT.size(), sizeof( resT[ 0 ] ), Cmp );

/*
	   	for (std::vector<pair<pair<string, string>, int> > ::const_iterator i = resT.begin(); i != resT.end(); ++i)
       if( (*i).second == resT[0].second)
	     std::cout << (*i).second<< " : " << ((*i).first).first<<"- "<< ((*i).first).second <<endl;
		
*/	   
		
	   cout<<"Case #"<<tc<<": "<<(resT[0].first).first<<" "<<(resT[0].first).second<<endl; 
	  
    }	
    

	return 0;
}
