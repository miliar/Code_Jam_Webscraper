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
#include <queue>          // std::queue
#include <deque>
using namespace std;


typedef stringstream ss;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef unsigned long long int64;

#define PI 3.14159265
#define pb push_back
#define ALL(t) t.begin(),t.end()
#define sz size()
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
//	freopen("D-small-attempt0.in", "r", stdin);	freopen("respuestaD_S.out", "w", stdout);	
	freopen("D-large.in", "r", stdin);	freopen("respuestaD_L.out", "w", stdout);

    int T;
    cin>>T;
    vd vA,vB,vT;
    int N;
	string val;
    double v;
    map<double, int> mR;
    deque<int> qA, qB;
    fornm(tc,1,T)
    {
          cin >> N;
          mR.clear();
          vA.clear();
          vB.clear();
          vT.clear();
		  qA.clear();
		  qB.clear();
    
          forn(i,N)
            {
               cin >> val;
			   v = toDouble(val);
               vA.pb(v);
               vT.pb(v);
            } 
          forn(i,N)
            {
               cin >> val;
			   v = toDouble(val);
               vB.pb(v);
               vT.pb(v);
            } 
          SORT(vT);
          SORT(vA);
          SORT(vB);
          forn(i,2*N)
             mR[vT[i]]=i+1;
          forn(i,N)
           { //cout<< mR[vA[i]] <<" - ";
             qA.pb(mR[vA[i]]);
           }
          forn(i,N)
           { //cout<< mR[vB[i]] <<" - ";
            qB.pb(mR[vB[i]]);
            }
            int resL = 0;  
            int a,b;
            while (qA.size()>0 && qB.size()>0 )
              {
                a= qA.front();
                qA.pop_front();
				if(qB.size()>0)
				  if(a<qB.front())
				    continue;
                while(qB.size()>0)
                {
                   b = qB.front();              
                   qB.pop_front();
                   if(a > b)
                   {  resL ++;
                      break;
                   }
                }
              }
          REVERSE(vA);
          REVERSE(vB);
          qA.clear();
          qB.clear();
          forn(i,N)
            qA.pb(mR[vA[i]]);
          forn(i,N)
           qB.pb(mR[vB[i]]);
           
           int resM = 0;  
           while (qA.size()>0 && qB.size()>0 )
              {
                a= qA.front();
                qA.pop_front();
				if(qB.size()>0)
				{
				  if(a>qB.front())
				   { 
                     resM++;
                     qB.pop_back();
                     continue;
                   }
                 else
                 {
                   qB.pop_front();  
                 }
				}
              }
            
      cout<<"Case #"<<tc<<": "<<resL<<" "<<resM<<endl;
    }
     return 0;
}

