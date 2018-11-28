//Bismillahir Rahmanir Rahim
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <stack>
using namespace std ;
#define MAXN
#define FOR(i,a,b) for(int i=(int) a ; i<=(int)b;i++)
#define inf 1000000
#define eps 10e-9
int main(int argc, char **argv){
	#ifdef unlucky_13
		freopen("B-large.bin","r",stdin) ;
		freopen("B-small-attempt0.out1","w",stdout) ;
	#endif
	ios_base::sync_with_stdio(false) ;
	int tc,ct=1 ;
	double C,F,X,tim,res,speed ;
	cin>>tc ;
	while(tc--){
		
		res = inf ;
		cin>>C>>F>>X ;
		tim = 0 ;
		speed = 2 ;
		while(1){
			res = min(res,tim+(X/speed)) ;
			tim += (C/speed) ;
			speed+=F ;
			if(tim>res) break ;
		}
		
		cout<<"Case #"<<ct++<<": " ;
		cout<<fixed<<setprecision(9)<<res+eps<<"\n" ;	
	}
		
	return 0;
}

