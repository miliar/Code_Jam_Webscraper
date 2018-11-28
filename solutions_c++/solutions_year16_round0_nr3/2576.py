
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
ll t,cas,d,i1,a,i2,r,v;
vi vk;
string wex;

string ms(ll z, ll d){
	string w;
	int i;

	w.assign(d,'0');
	i=1;
	while(z>0){
		w[d-i]=z%2+'0';
		z/=2;
		i++;
	}
	return w;

}
ll dob(string wex, ll b){
	ll z,k,a,i;

	a=1;
	k=wex.size();

	z=a;
	for(i=1;i<=k;i++){
		a*=b;
		z+=(wex[k-i]-'0')*a;
	}
	a*=b;
	z+=a;
	if(z%(b+1)==0)
		return z;
	return -z;
	

}
int main() {  
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin); 
	
	//pi=2*acos(0.0); 
	//while(1){
	//vk.clear(); 
	//d=1000000007; 
	
		
	
	cin>>t;
	for(cas=1;cas<=t;cas++){
		
		cin>>n>>k;
		
		z=0;
		wex=ms(z,n-2);
		cout<<"Case #"<<cas<<":"<<endl;
		j=0;
		while(j<k){
	//	for(j=0;j<k;j++){

			
			//spr
			d=0;
			for(b=2;b<=10;b++){
				if(dob(wex,b)>0){
					
				//	cout<<z<<" OK"<<endl;
				}
				else {
					d=1;
					break;
				
				//	cout<<z<<" BLAD "<<b<<endl;
				}
			}
			if(d==0){
				cout<<"1"<<wex<<"1";
				for(i=3;i<=11;i++)
					cout<<" "<<i;
				cout<<endl;
				j++;
			}


			//spr koniec
			z+=3;
			wex=ms(z,n-2);
		}



		
	}

	return 0;

} 


