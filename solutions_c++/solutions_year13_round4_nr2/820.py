#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <math.h>
#include <cstring>
#include <gmp.h> // shiny bigint library from http://gmplib.org

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPA(i,a,n) for(int i=(a);i<((a)+(n));i++)
#define INITW(var,value,width) for(int whslkfje=0;whslkfje<(width);whslkfje++) var[whslkfje]=(value)
#define INITHW(var,value,height,width) for(int hwesaft=0;hwesaft<(height);hwesaft++) \
		 for(int whslkfje=0;whslkfje<(width);whslkfje++) var[hwesaft][whslkfje]=(value)

typedef long long lint;
using namespace std;
void solve();
void init();

int main(){
	init();

	int T;
	cin>>T;
	string str;
	getline(cin, str);
	
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		solve();
		cout<<"\n";
	}
}

void init(){
	
}

lint getmax(lint P, lint N){
	lint teams = (1<<N);
	if(P==teams)return teams-1;
	if(P==1)return 0;
	
	lint intn = 0;
	lint inkl = 1;
	while(P>inkl){
		intn++;
		inkl+=(inkl+1);
	}
	lint toadd = teams/2;
	lint res=0;
	while(intn>0){
		res+=toadd;
		toadd/=2;
		intn--;
	}
	return res;
}

lint getmin(lint P, lint N){
	lint teams = (1<<N);
	if(P==teams)return teams-1;
	if(P==1)return 0;
	
	lint ones = 1;
	while(2*P > teams){
		teams /= 2;
		P -= teams;
		ones++;
	}
	lint res=0;
	while(ones>0){
		res*=2;
		res++;
		ones--;
	}
	return res-1;
}
		
void solve(){
	lint N,P;
	cin>>N>>P;
	/*
	lint teams = (1<<N);
	lint min = 0;
	while(P>teams * (1-1.0/(1<<min)))min++;
	* */
	cout<<getmin(P,N)<<" "<<getmax(P,N);
}
