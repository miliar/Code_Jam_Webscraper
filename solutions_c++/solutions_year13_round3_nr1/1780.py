
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h> 
#include <map>  
#include <string>
#include <vector> 
#include <list>
#include <iostream>   
#include <sstream> 
#include <queue> 
#include <algorithm>

using namespace std; 
 
#define PB 		push_back
#define FOR(a,start,end) 	for(int a=int(start); a<int(end); a++)
#define INF 		INT_MAX
#define SORT(a) 	sort(a.begin(),a.end())
#define CL(a,x) 		memset(a,x,sizeof(a))
#define REP(a,x)	for(int a=0;a<x;a++)
#define REP1(a,x)	for(int a=1;a<=x;a++)
#define MP 		make_pair
#define vi vector<int>
#define vvi vector<vector<int> >
#define vii vector<pair<int,int> >
#define vvii vector<vector<pair<int,int> > >
#define pii pair<int,int>
#define vs vector<string>

int i,k,j,n,r,c,i1,m,s,g,z1; 
int cas,a,b,z,w,d,h,t,zmin;
int amin,amax,bmin,bmax;

vii vp;
vvii vz; 
pii p1,p2;
 
string we,we1,we2,wex;
vi vk,va,vb;
vs tt;


int main() { 
//	freopen( "c:\\wojtek\\uva\\uva\\debug\\tal0.in", "rt", stdin); 
	//	int czas=clock(); 
	//pi=2*acos(0.0);

	//d=1000000007;
	
	
	cin>>t;


	for(cas=1;cas<=t;cas++){
		z=0;	
		cin>>we>>k;
		
		n=we.size();
		d=0;
		i=0;
		b=-1;
			for(j=i;j<i+k;j++){
				if(we[j]=='a'||we[j]=='e'||we[j]=='i'||we[j]=='o'||we[j]=='u')
					continue;
				else
					d++;
			}
		if(d==k){
				z+=i+1;
				z+=n-i-k;
				b=0;
			}
		for(i=1;i<=n-k;i++){
			j=i-1;
			if(we[j]=='a'||we[j]=='e'||we[j]=='i'||we[j]=='o'||we[j]=='u'){}
			else
				d--;
			j=i+k-1;		
			if(we[j]=='a'||we[j]=='e'||we[j]=='i'||we[j]=='o'||we[j]=='u'){}
			else
				d++;
					 
			if(d==k){
				z+=(i-b)*(n-i-k+1);
			//	z++;
				
				
				b=i;
			}
		}

			
		cout<<"Case #"<<cas<<": "<<z<<endl;
		
	
	}

	
		
//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
