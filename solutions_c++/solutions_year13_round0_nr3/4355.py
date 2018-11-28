#include <iostream>
#include <algorithm>
#include <string>
#include <math.h>
#include <fstream>
using namespace std;
#define fon(i,n) for(i=0;i<n;++i)
#define re return
#define ll long long
const double EPS = 1E-9;const int INF = 1000000000;const ll INF64 = (ll)1E18;const double PI = 3.1415926535897932384626433832795;

bool isPol(ll num){
	ll numCopy=num,numRev=0;
	while(numCopy>0){
		numRev=numRev*10+numCopy%10;
		numCopy/=10;
	}
	re (numRev==num);
}
ll getPol(ll polHalf){
	ll res,half2=0,polCopy,t10=1;
	for(polCopy=polHalf;polCopy>0;polCopy/=10,t10*=10)
		half2=half2*10+polCopy%10;
	if(!isPol(half2*t10+polHalf))re 0;
	re half2+polHalf*t10;
}
ll getPol2(ll polHalf){
	ll res,half2=0,polCopy,t10=1;
	if(polHalf<10)re polHalf;
	for(polCopy=polHalf/10;polCopy>0;polCopy/=10,t10*=10)
		half2=half2*10+polCopy%10;
	if(!isPol(half2*t10+polHalf))re 0;
	re half2+polHalf*t10;
}
ll bs(ll A,ll B){
	ll l=sqrt(1+sqrt((double)A))-100,r=sqrt(1+sqrt((double)B))+100;
	if(l<0)l=0;
	ll lNum,rNum,sum=0;
	for(;l<r;++l){
		lNum=getPol(l);lNum*=lNum;
		if(lNum>B)re sum;
		if(lNum>=A&&isPol(lNum))++sum;//cout<<lNum<<endl;
	}re sum;
}
ll bs2(ll A,ll B){
	ll l=sqrt(sqrt((double)A))-100,r=sqrt(1+sqrt((double)B))+100;
	if(l<0)l=0;
	ll lNum,rNum,sum=0;
	for(;l<r;++l){
		lNum=getPol2(l);lNum*=lNum;
		if(lNum>B)re sum;
		if(lNum>=A&&isPol(lNum))++sum;
	}re sum;
}
int main()
{
	#ifndef ONLINE_JUDGE
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	#endif

	ll i,j,n,m,T,t,k;
	ll A,B;
	cin>>T;
	for(t=0;t<T;++t){
		cin>>A>>B;
		cout<<"Case #"<<t+1<<": "<<bs(A,B)+bs2(A,B)<<endl;
	}
	re 0;
}