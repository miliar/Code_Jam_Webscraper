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


    int T, n;
    cin>>T;
    string str;
    int a,b;
	set<int> res;	
    fornm(tc,1,T)
    {
		cin >> a;
		a--;
		int A[4][4];
		int B[4][4];
		int L[4];
       res.clear();
		memset(A,0,sizeof(A));
		memset(B,0,sizeof(B));
		memset(L,0,sizeof(L));
		forn(i,4)
		  forn(j,4)
		  {
		  cin >> A[i][j];
		  }
		cin >> b;
		b--;
		forn(i,4)
		  forn(j,4)
		  {
		    cin >> B[i][j];
			}
			
			
		forn(k,4)
		 {
		   res.insert(A[a][k]);
		 }
		 forn(k,4)
		 {
		   res.insert(B[b][k]);
		 }
	     if(res.size()==8)
			cout<<"Case #"<<tc<<": Volunteer cheated!"<<endl;
		else if(res.size()<7)
			cout<<"Case #"<<tc<<": Bad magician!"<<endl;
		else
		{
		bool listo = false;
		forn(i,4)
			forn(j,4)
			{
			   if(A[a][i]==B[b][j])
			    {
				   cout<<"Case #"<<tc<<": "<<A[a][i]<<endl;
				   listo =  true;
				   break;
				}
			}
		}
		   
		
		 
    }	
    

	return 0;
}
