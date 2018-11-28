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

int dx[]={1,1,0},dy[]={0,1,1};
#define MAXIMO 10000

string s;

int main()
{
//	freopen("A-small-attempt0.in", "r", stdin); 	freopen("respuestaA_S.out", "w+", stdout);
	freopen("A-large.in", "r", stdin);  	freopen("respuestaA_L.out", "w+", stdout);


    int T;
    cin>>T;
    
    
    
    
    fornm(tc,1,T)
    {
	    cin >> s;
		vi r;
		
		int n=0;
		int rr=0;
		int v=0;
		int f = 0;int ii =0;
		forn(i,s.length())
		{
			if(s[i] == 'N') n++;
			if(s[i] == 'R') rr++;
			if(s[i] == 'V') v++;
			if(s[i] == 'F') f++;
			if(s[i] == 'I') ii++;
			if(s[i] == 'Z'){
			rr--;r.pb(0);}
			if(s[i] == 'W')r.pb(2);
			if(s[i] == 'X'){
				ii--;
			r.pb(6);}
			if(s[i] == 'G'){
			ii--;r.pb(8);}
			if(s[i] == 'U'){
			f--;rr--;
			r.pb(4);
	    	}
		
			
		}
		forn(i,f)
		{
			r.pb(5);
			ii--;
			v--;
		}
		forn(k,v)
			{
			r.pb(7);
			n--;
		   }
		
		if(ii>0)
	     forn(k,ii){
		 n--;n--;
		 r.pb(9);}
	   forn(k,n)r.pb(1);
	   forn(k,rr)r.pb(3);
	   
	   /*
		cout<<f<<" "<<v<<endl;
		if(f==v && f >0)
		{
			forn(k,f){
			ii--;
			r.pb(5);}
		}
		else if(v-f > 0)
		{
		
			forn(k,v-f)
			{
			r.pb(7);
			n--;v--;
		   }
			forn(k,v){
			ii--;
			r.pb(5);}
	   }
	     */
	   SORT(r);
		cout<<"Case #"<<tc<<": ";
		
		for (std::vector<int>::const_iterator i = r.begin(); i != r.end(); ++i)
         std::cout << *i ;
		
		cout<<endl; 
      }
	
	
    	
    

	return 0;
}
