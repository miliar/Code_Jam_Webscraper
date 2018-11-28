
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
#define FOR(a,start,end) 	for(long long a=long long(start); a<long long(end); a++)
#define INF 		INT_MAX
#define SORT(a) 	sort(a.begin(),a.end())
#define CL(a,x) 		memset(a,x,sizeof(a))
#define REP(a,x)	for(long long a=0;a<x;a++)
#define REP1(a,x)	for(long long a=1;a<=x;a++)
#define MP 		make_pair
#define vi vector<long long>
#define vvi vector<vector<long long> >
#define vii vector<pair<long long,long long> >
#define vvii vector<vector<pair<long long,long long> > >
#define pii pair<long long,long long>
#define vs vector<string>

long long z2,z3,z1,i,k,j,n,r,c,i1,m,s,g,b0; 
long long d0,cas,a,b,z,w,d,h,t,b1;
long long amin,amax,bmin,bmax;

vii vp;
vvii vz; 
pii p1,p2;
 
string we,we1,we2,wex;
vi vk,va,vb;
vvi vvt;
vs tt;
long long ta[200];

string konw(long long a){
	int i,k;
	string w1,w2;

	w1.clear();
	w2.clear();

	while(a>0){
		w1+=a%10+'0';
		a/=10;
	}
	k=w1.size();
	for(i=k-1;i>=0;i--){
		w2+=w1[i];
	}
	return w2;
}


int czyp(long long a){
	int i,k;
	string w1;

	k=0;
	
	w1=konw(a);
	k=w1.size();

	for(i=0;i<=k/2;i++){
		if(w1[i]!=w1[k-1-i])
			return 0;
	}
	return 1;
}




	


int main() { 
	freopen( "c:\\wojtek\\uva\\uva\\debug\\tcs1.in", "rt", stdin); 
	//	long long czas=clock(); 
	//pi=2*acos(0.0);

	//d=1000000007;  
	 
	CL(ta,0);

	n=9;
	ta[1]=n;
	ta[2]=n;
	for(i=3;i<20;i+=2){
		n*=10;
		ta[i]=n;
		ta[i+1]=n;
	}


	cin>>t;
	
	for(cas=1;cas<=t;cas++){
		cin>>a>>b;

		d=(long long)sqrt((double)b);
		if((d+1)*(d+1)<=b)
			d++;
		
		k=0;
		c=d;
		while(c>0){
			k++;
			c/=10;
		}

		z=0;
		for(i=1;i<k;i++)
			z+=ta[i];

		we1=konw(d);

		
		for(i=0;i<=k-i-1;i++){
			if(we1[i]>we1[k-1-i])
				we1[i]--;
			we1[k-1-i]=we1[i];
		}

		z1=min(we1[0],we1[k-1])-'0';

		for(i=1;i<=k-1-i;i++){
			z1*=min(we1[i],we1[k-1-i])-'0'+1;
		}


		z+=z1;

		d0=(long long)sqrt((double)a);
		if((d0+1)*(d0+1)<=a)
			d0++;
		if(d0*d0==a)
			d0--;
		k=0;
		c=d0;
		z2=0;
		if(c==0)
			z3=0;
		else {
			while(c>0){
				k++;
				c/=10;
			}

			z2=0;
			for(i=1;i<k;i++)
				z2+=ta[i];

			we1=konw(d0);

			for(i=0;i<=k-1-i;i++){
				if(we1[i]>we1[k-1-i])
					we1[i]--;
				we1[k-1-i]=we1[i];
			}

			z3=min(we1[0],we1[k-1])-'0';



			for(i=1;i<=k-1-i;i++){
				z3*=min(we1[i],we1[k-1-i])-'0'+1;
			}
		}

		z2+=z3;

		z-=z2;

		for(i=d0+1;i<=d;i++){
			if(czyp(i)&&(!czyp(i*i)))
				z--;
		}
		
		cout<<"Case #"<<cas<<": "<<z<<endl;
		
	



	
	}

	
		
//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
