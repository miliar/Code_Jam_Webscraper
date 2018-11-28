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

int dx[]={0,0,0,0,0,0,0,0,0,0,0};
#define MAXIMO 10000


int64 guarda(int64 numero)
{
 
        while(numero>0)
        {
         dx[numero%10]=1; //Obtenemos cada uno de los dígitos
         numero=numero/10;
        }
        int64 res = 0;
        for(int i=0;i<10;i++)
          res += dx[i];
                
                        
      return res;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); 	freopen("respuestaA_S.out", "w+", stdout);
	freopen("A-large.in", "r", stdin);  	freopen("respuestaA_L.out", "w+", stdout);


   int64 T,k;
    cin>>T;
	fornm(tc,1,T)
    {
	     cin>> k;
	     int64 n = 1;
	     memset(dx,0,sizeof(dx));
	     if(k== 0)
	     {
			  cout<<"Case #"<<tc<<": INSOMNIA"<<endl;
			  continue;
		}
	     while( guarda(n*k) != 10)
		 {
		   n++;
		 }
       cout<<"Case #"<<tc<<": "<<(n)*k<<endl;
           
	}
    

	return 0;
}
