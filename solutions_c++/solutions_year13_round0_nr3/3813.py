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

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 2000000

int dig=1;
int Res[MAXIMO];

vector<int64> Primos;
vector<int64> Primos2;
set<int64> Ops;
void primos(int64 numero)
{
  int cont,k=0;
  bool sigue=true;
  for(int64 i=13;i<=numero;i+=2)
  {
    cont=0;
    k=0;
    sigue=true;
				while(Primos[k]*Primos[k]<i+1 && sigue)
				{
					if(i%Primos[k]==0)sigue=false;
				k++;
				}
    if(sigue)Primos.pb(i);
  }
}
unsigned long long invierte(unsigned long long numero)
{
unsigned long long numeroinv=0;
int nums[100];
int pos=0;int pow=1;

		forn(i,100)nums[i]=0;
		
		while(numero>0)
		{
	     nums[pos++]=numero%10;
	     numero=numero/10;
		}
		for(int i=pos-1;i>-1;i--)
		{
		     	numeroinv += pow*nums[i];
					 pow *=10;			
	  } 				 
	  return numeroinv;
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);	freopen("respuesta1S.out", "w", stdout);	
//	freopen("C-large.in", "r", stdin);	freopen("respuestaL.out", "w", stdout);

    int T,cont;
	int64 A,B,maxP,minP;
   Primos.clear();
   Primos.pb(2);
   Primos.pb(3);
   Primos.pb(5);
   Primos.pb(7);
   Primos.pb(11);
   //primos(10000000);
   primos(10000);

  Primos2.pb(1);
  forn(i,Primos.size())
	  Primos2.pb(Primos[i]*Primos[i]);
  Ops.clear();
	  // TODOS HASTA 1000
	  int maxB = 1000;
	  bool next=true;
	  forn(i,Primos2.size())
	   {
	   	
	   	if(maxB<Primos2[i]*Primos2[0])
			{
			break;
		    }
	   	forn(j,Primos.size())
	   	{
	   		int64 n=Primos2[i]*Primos2[j];
	   	    
	   		if(n==invierte(n))
			 {
			 	int64 n2 = sqrt(n);
			 	if(n2 == invierte(n2))
			 		Ops.insert(n);
			}   
	   	}
	   }
	  std::set<int64>::iterator it;
	 //   for (it=Ops.begin(); it!=Ops.end(); ++it)
       //      cout << ' ' << *it;
    cin>>T;
    fornm(tc,1,T)
    {
      cin >> A >> B;
      cont=0;
      for (it=Ops.begin(); it!=Ops.end(); ++it)
      {
      	int64 n = *it;
      	if(A<=n && n<=B)
      	 cont++;
      	if(n>B)break;
      }
      
   	// print cases
      cout<<"Case #"<<tc<<": "<<cont<<endl;
     }
     
     
     return 0;
}
