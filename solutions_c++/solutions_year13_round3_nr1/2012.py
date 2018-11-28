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
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef vector< vi > matrix;

#define pb push_back
#define fornm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define pb push_back
#define all(v) v.begin(),v.end()
#define sort(c) sort(all(c))
#define reverse(c) reverse(all(c))
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define ordC(v,cpm) qsort( (void *)&v[0], v.size(), sizeof( v[ 0 ] ), cpm )

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000

string ops="bcdfghjklmnpqrtsvwxyz";
set<char> vOps;
int tiene(string s)
{
	int cont=0;
	bool flag=false;
	int max=-1;
	forn(i,s.length())
	  {
	  	if(vOps.find(s[i])!=vOps.end())
	  	{
	  		flag = true;
	  		cont++;
	  	}
	  	else if(flag)
	  	{
	  		if(max<cont)max=cont;
	  	  cont=0;
	    }
	  }
	  if(max<cont)max=cont;
	return max;
}
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);	freopen("respuestaA-S.out", "w", stdout);	
//	freopen("A-large.in", "r", stdin);	freopen("respuestaA-L.out", "w", stdout);

vOps.insert('q');
vOps.insert('w');
vOps.insert('r');
vOps.insert('t');
vOps.insert('y');
vOps.insert('p');
vOps.insert('s');
vOps.insert('d');
vOps.insert('f');
vOps.insert('g');
vOps.insert('h');
vOps.insert('j');
vOps.insert('k');
vOps.insert('l');
vOps.insert('z');
vOps.insert('x');
vOps.insert('c');
vOps.insert('v');
vOps.insert('b');
vOps.insert('n');
vOps.insert('m');
	int T,N;
	cin>>T;
	string s;
	int val;
	set<pair<int,int> > listo;
	fornm(tc,1,T)
    {
    	cin>> s;
    	cin >> val;
    	int L = s.length();
    	int cont =0 ;
    	
    	listo.clear();
    	forn(i,L)
    	fornm(j,i,L-1)
    	{
    	if(listo.find(make_pair(0,i) )== listo.end())
   		  {
   		   if(tiene(s.substr(0,i))>=val)
    	     cont++;
    	listo.insert(make_pair(0,i) );
        }
        if(listo.find(make_pair(i,j-i)) == listo.end())
   		  {
    		if(tiene(s.substr(i,j-i))>=val)
    			  cont++;
    		listo.insert(make_pair(i,j-i) );
    	}
    	if(listo.find(make_pair(j,L))== listo.end())
   		  {
    		if(tiene(s.substr(j))>=val)
    			  cont++;
    		listo.insert(make_pair(j,L) );
    	}
    	}

      cout<<"Case #"<<tc<<": "<<cont<<endl;
	}
	return 0;
}

