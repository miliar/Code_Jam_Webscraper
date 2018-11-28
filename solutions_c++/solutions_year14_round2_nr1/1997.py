
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
 
#define ll long long
#define PB 		push_back
#define FOR(a,start,end) 	for(int a=int(start); a<int(end); a++)
#define INF 		int_MAX
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
int s,c,i,k,j,n,m,z,jx,z0,b,a0,b0,z1; 
int t,cas,i1,i2,i3;
vvi vvk,vvc;
vii vp,vp2;
pii p1,p2;
vector<pair<int,int> > vpk;
vs ve;
string wy,wyb,we;
vs vsl,vt;
vi vk,vk1,vk2,vm,vc;
int k1,k2,k3,p;
int a1,a2;
vector<int> vz,vz2;
int zx,d,d2,d1,a,r;
vector<pair<char,int> > vkc;
vector<vector<pair<char,int> > > vvkc;
char zn;
double dx,ax;


int main() {  
	freopen( "c:\\wojtek\\uva\\uva\\debug\\a0.in", "rt", stdin); 
	
	//pi=2*acos(0.0);
	//while(1){
	//	vk.clear(); 
	//d=1000000007; 
	 
	cin>>t;
	//scanf("%d",&t); 

	for(cas=1;cas<=t;cas++){
		
		cin>>n;
		vt.clear();
		for(i=0;i<n;i++){
			cin>>we;
			vt.push_back(we);
		}
		vkc.clear();
		vvkc.clear();
		i=0;
		k=vt[0].size();
		zn=vt[0][0];
		j=0;
		while(i<k){
			while(i<k&&vt[0][i]==zn){
				i++;
			}
			vkc.push_back(MP(zn,i-j));
			j=i;
			if(i<k)
				zn=vt[0][i];
		}
		vvkc.push_back(vkc);
		zx=0;
		for(i1=1;i1<n;i1++){
			vkc.clear();
			i=0;
			k=vt[i1].size();
			zn=vt[i1][0];
			j=0;
			while(i<k){
				while(i<k&&vt[i1][i]==zn){
					i++;
				}
				vkc.push_back(MP(zn,i-j));
				j=i;
				if(i<k)
					zn=vt[i1][i];
			}
			z=0;
			if(vkc.size()==vvkc[0].size()){
				for(i=0;i<vkc.size();i++){
					if(vkc[i].first!=vvkc[0][i].first){
						z=1;
						break;
					}
				}
			}
			else
				z=1;
			if(z==1){
				zx=1;
				
			}
			else {

				vvkc.push_back(vkc);
			}

		}
		if(zx==1)
	
			cout<<"Case #"<<cas<<": "<<"Fegla Won"<<endl;
		else {
			k=0;
			for(i=0;i<vvkc[0].size();i++){
				z=0;
				a1=0;
				a2=0;
				for(j=0;j<vvkc.size();j++){
					z+=vvkc[j][i].second;
				}
				dx=(double)z/(double)n;
				a=floor(dx);
				b=ceil(dx);
				for(j=0;j<vvkc.size();j++){
					a1+=abs(vvkc[j][i].second-a);
					a2+=abs(vvkc[j][i].second-b);
				}
				k+=min(a1,a2);
			}
	
			cout<<"Case #"<<cas<<": "<<k<<endl;
		}

	}



	return 0;

} 
