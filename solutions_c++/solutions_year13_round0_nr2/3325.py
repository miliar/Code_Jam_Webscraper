
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

int i,k,j,n,r,c,i1,m,s,g,b0; 
int cas,a,b,z,w,d,h,t,b1;
int amin,amax,bmin,bmax;

vii vp;
vvii vz; 
pii p1,p2;
 
string we,we1,we2,wex;
vi vk,va,vb;
vvi vvt;
vs tt;


int main() { 
	freopen( "c:\\wojtek\\uva\\uva\\debug\\tbl.in", "rt", stdin); 
	//	int czas=clock(); 
	//pi=2*acos(0.0);

	//d=1000000007; 
	 
	
	cin>>t;
	
	for(cas=1;cas<=t;cas++){
		cin>>n>>m;
		vvt.clear(); 
		for(i=0;i<n;i++){
			vk.clear();
			for(j=0;j<m;j++){
				cin>>a;
				vk.push_back(a);
			}
			vvt.push_back(vk);
		}
		
		a=1;
		for(i=0;i<n;i++){
			z=0;
			b=vvt[i][0];
			for(j=0;j<m;j++){
				b=max(b,vvt[i][j]);
			}
			for(j=0;j<m;j++){
				if(vvt[i][j]<b){
					b1=vvt[i][j];
					for(i1=0;i1<n;i1++){
						if(vvt[i1][j]>b1){
							z=1;
							break;
						}
					}
				}
				if(z==1)
					break;
			}
			if(z==1)
				break;
		}






		if(z==0)
			cout<<"Case #"<<cas<<": "<<"YES"<<endl;
		
		else
			cout<<"Case #"<<cas<<": "<<"NO"<<endl;


 



	
	}

	
		
//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
