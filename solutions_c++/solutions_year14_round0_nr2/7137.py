/*
ID: abunida1
PROG: ride
LANG: C++
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <math.h>
#include <stack>
#include <bitset>
#include <list>
#include <limits.h>

using namespace std;


#define ii pair<int,int>
#define iii pair<int,ii>
#define INF 1000000000
typedef long long int ll;
typedef unsigned long long int ull;
typedef vector <int> vi;
typedef vector <ii> vii;

double c,f,x;//harga kelipatan finish
double awal=2.0;

double cek (int beli) {
	
	double waktu=0.0;
	
	int punya=0;
	
	while(beli!=punya){
		waktu+=c/( awal + (double)punya*f ) ;
		punya++;
	}
	
	waktu+=x/( awal + (double)punya*f ) ;
	
	return waktu;
}


int main (){

	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	//freopen("friday.in","r",stdin);	freopen("friday.out","w",stdout);
	
	c=500.0;
	f=4.0;
	x=2000.0;
	
	//printf("%.7llf\n",cek(3));
	
	int t;
	
	scanf("%d",&t);
	int kasus=1;
	
	
	
	while(t--){
		printf("Case #%d: ",kasus);kasus++;
		
		double past,next;
		double ans;
		cin>>c>>f>>x;
		
		ans=past=cek(0);
		
		for(int i=1;;i++){
			next=cek(i);
			ans=min(ans,next);
			if(past<=next)break;
			past=next;
		}
		
		printf("%.7llf\n",ans);
		
	}

	
	return 0;
}
















