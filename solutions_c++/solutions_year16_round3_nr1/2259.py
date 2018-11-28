
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
ll s,c,i,k,j,n,m,z,b; 
ll t,cas,d,i1,a,i2,r,w;
ll ta[10];
vii vk,vk2;
string wy;

int main() {  
//	freopen( "c:\\wojtek\\uva\\uva\\debug\\a0.in", "rt", stdin); 
	
	//pi=2*acos(0.0); 
	//while(1){
	//vk.clear(); 
	//d=1000000007; 
	
		
	
	cin>>t;
	
	for(cas=1;cas<=t;cas++){
		vk.clear();
		cin>>n;
		wy.clear();
		for(i=0;i<n;i++){
			cin>>a;
			vk.push_back(MP(a,i));
		}
		SORT(vk);
		while(vk.size()>0){
			k=vk.size();
			if(vk.size()==2&&vk[0].first==1&&vk[1].first==1){
				wy+=vk[k-1].second+'A';
				wy+=vk[k-2].second+'A';
				vk.clear();
			}
			else if(vk.size()==2&&vk[0].first==vk[1].first){
				wy+=vk[k-1].second+'A';
				wy+=vk[k-2].second+'A';
				vk[k-1].first--;
				vk[k-2].first--;
				if(vk[k-1].first==0)
					vk.clear();
			}
			else if(vk.size()==2&&vk[0].first!=vk[1].first){
				wy+=vk[k-1].second+'A';
				
				vk[k-1].first--;
				
			}
			else {

			
				if(vk[k-1].first-vk[k-2].first>=1){
					wy+=vk[k-1].second+'A';
					wy+=vk[k-1].second+'A';
					
					vk[k-1].first-=2;
					if(vk[k-1].first==0)
						vk.pop_back();
				}
				else {
					if(vk[k-1].first==1){
						wy+=vk[k-1].second+'A';
					
					vk[k-1].first--;
					if(vk[k-1].first==0)
						vk.pop_back();
				
					}
					else {

					wy+=vk[k-1].second+'A';
					
					wy+=vk[k-2].second+'A';
					vk[k-2].first--;
					vk[k-1].first--;
					if(vk[k-1].first==0)
						vk.pop_back();
					if(vk[k-2].first==0)
						vk.pop_back();
					}
				}
				
				
			}
			wy+=' ';
				SORT(vk);
			
		}


		cout<<"Case #"<<cas<<": "<<wy<<endl;
		

	}
		
	return 0;

} 


