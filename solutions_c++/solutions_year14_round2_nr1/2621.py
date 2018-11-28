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


int main()
{
	freopen("A-small-attempt0.in", "r", stdin); 	freopen("respuestaA_S.out", "w+", stdout);
//	freopen("A-large.in", "r", stdin);  	freopen("respuestaA_L.out", "w+", stdout);


    int T, N;
    cin>>T;
    
    fornm(tc,1,T)
    {
	    cin >> N ;
		string S ;
		vs vS(N);
		forn(i,N)
		   cin >> vS[i];
       
	   vector<vector<int> > cS(N+1);
	   vector<vector<char> > cC(N+1);
		forn(i,N)
		{
		   string st = vS[i];
		   char t = st[0];
		   int cont = 0;
		   forn(k,st.length())
		   {
		      if(t != st[k])
			  {
                   cS[i].pb(cont);
			     cC[i].pb(t);
                 t = st[k];
			     cont = 1;
			  }
			  else
			   cont++;
		      
		   }
		   cS[i].pb(cont);
	       cC[i].pb(st[st.length()-1]);
		   
		}
		
		int res = 1000000;
		bool termino = false;
		int  sum = 0;
		forn(i,N)
		{
		  int dist = 0;
		  if(termino ) break;
		  sum = 0;
		  forn(j,N)
		  {
		     if(termino)break;
		     
		     if(j!=i)
		     {
				 forn(k,cS[i].size())        
				 {
					if(cC[i][k]!=cC[j][k])
					{
					   termino = true;
					   break;
					}
					  sum +=abs(cS[i][k]-cS[j][k]);
				 }   
			 }
		   }
		 	if(sum <= res)
			res = sum;
    		
         }
		 sum = 0;
		 forn(i,N)
		{
		  	 forn(k,cS[i].size())        
				 {
					  sum +=abs(cS[i][k]-1);
				 }   
			
		   }
		   if(sum <= res)
			res = sum;
		
		if(termino)
        cout<<"Case #"<<tc<<": Fegla Won"<<endl; 
		else
		cout<<"Case #"<<tc<<": "<<res<<endl; 
		
	
    }	
    

	return 0;
}
