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
//	freopen("A-small-attempt0.in", "r", stdin); 	freopen("respuestaA_S.out", "w+", stdout);

	freopen("A-large.in", "r", stdin);  	freopen("respuestaA_L.out", "w+", stdout);


   int T,k;
    cin>>T;
	string str;
	int res = 0;
	int ready = 0;
    fornm(tc,1,T)
    {
	     cin>> k>> str;
	     res=0;
	     ready = 0;
         for(int  i=0; i<k+1;i++) 
         {
                  
           int c = str[i]-'0';
           
           if(ready < i)
            {
              res += (i-ready); 
              ready+= (i-ready); 
           }
           ready+=c;
         }
       cout<<"Case #"<<tc<<": "<<res<<endl;
           
	}
    

	return 0;
}
