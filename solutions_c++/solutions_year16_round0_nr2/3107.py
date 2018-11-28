
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
#include <fstream>
#include <iomanip>


using namespace std; 

#define INF 2000000000
#define FT first
#define SD second
#define PB push_back
#define ll long long
#define PB 		push_back
#define FOR(a,start,end) 	for(int a=int(start); a<int(end); a++)
//#define INF 		int_MAX
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
ll s,c,i,k,j,n,m,z,b,l; 
ll t,cas,d,i1,a,i2,r,z1,dl;
double ax,dx,bx,cx,gx;
int ta[30];
string we,wex;




int main() {  
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin); 
	
	//pi=2*acos(0.0); 
	//while(1){
	//vk.clear(); 
	//d=1000000007; 
	
		
	
	cin>>t;
	for(cas=1;cas<=t;cas++){

		cin>>we;
		k=we.size();
		z=0;

		i=0;
		a=0;
		while(i<k){
			if(we[i]=='+'){
				a=1;
				while(i<k&&we[i]=='+'){
					i++;
				}
			}
			if(i<k){
				while(i<k&&we[i]=='-'){
					i++;
				}
				z+=a+1;
			}
		}

		
	//	cout<<setprecision(9);
		cout<<"Case #"<<cas<<": "<<z<<endl;
	}

	return 0;

} 


