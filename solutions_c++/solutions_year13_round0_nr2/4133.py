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
#define ALL(t) t.begin(),t.end()
#define fornm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000
int main()
{
//	freopen("B-small-attempt0.in", "r", stdin);	freopen("respuestaS.txt", "w+", stdout);

	freopen("B-large.in", "r", stdin);	freopen("respuestaL.out", "w+", stdout);

	
    int T,cont;
    string str;
    int V[101][101];  
    bool Vbln[101][101];  
    int maxH[101],maxV[101];
    cin>>T;
    int N,M,num;
    fornm(tc,1,T)
    {
       cin >> N >> M;
       
    memset(V,0,sizeof(V));
    memset(Vbln,false,sizeof(Vbln));
    memset(maxH,-1,sizeof(maxH));
    memset(maxV,-1,sizeof(maxV));
     forn(i,N)
     {
        
        forn(j,M)
       {
       	cin >> num;
       	V[i][j]=num;
       	if(maxH[i]<=num)
       	   maxH[i]=num;
        }
     }   
     forn(i,N)
     {
     	forn(j,M)
     	{
     		if(V[i][j]==maxH[i])
     		  Vbln[i][j]=true;
     	}
     }
     forn(j,M)
     {
     	forn(i,N)
     	{
     	
     		if(maxV[j]<=V[i][j])
     		 maxV[j]=V[i][j];
     	}
     }
     forn(j,M)
     {
     	
     	forn(i,N)
     	{
     		if(maxV[j]<maxH[i])
     		{
     		   if(V[i][j]==maxV[j])
     		     Vbln[i][j]=true; 
			}
     	}
     }
    
      int cont=0;
      forn(i,N)
       forn(j,M)
          if(!Vbln[i][j])cont++;
    
      	if(cont==0)
		   cout<<"Case #"<<tc<<": YES"<<endl;
		else
		   cout<<"Case #"<<tc<<": NO"<<endl;

	}
	return 0;
}

