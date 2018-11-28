#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <iomanip> 
#include <vector>
#include <list>
#include <utility> 
#include <iterator> 
#include <math.h> 
#include <algorithm> 
#include <stdio.h> 
using namespace std;


#define REP(i,T) for(int i=0;i<T;++i)
#define MP make_pair
#define PII pair<int,int>
#define BG begin
#define ND end
#define VI vector<int>
#define VB vector<bool>
#define ALL(i) i.BG(),i.ND()
#define FORI(i,a,b) for(int i=a;i<b;++i)
#define OUT(i) while(!i.empty())
#define GP(a,b) a[b.first][b.second]
#define EX(a,b) (a.find(b)!=a.end())

int getDWar(vector<double> x,vector<double> y){
	int c=0,i,j;
	for(i=0,j=0;i<x.size();++i){
		if(x[i]>y[j]){
			c++;
			j++;
		}
	}
	return c;
}
/*
int getWar(vector<double> x,vector<double> y){
	int c=0,i,j;
	for(i=0,j=0;i<x.size();++i){
		if(x[i]>y[j]){
			c++;
			j++;
		}
	}
	return c;
}*/
void judge(){
	int  n;
	scanf("%d",&n);
	vector<double> x(n),y(n);
	REP(i,n)cin>>x[i];
	REP(i,n)cin>>y[i];
	sort(ALL(x));
	sort(ALL(y));
	printf("%d ",getDWar(x,y));
	printf("%d",n-getDWar(y,x));

	return;


}
int main(){
	int t;
	scanf("%d",&t);
	REP(tt,t){
		cerr<<tt<<endl;
		printf("Case #%d: ",tt+1);
		judge();
		
		printf("\n");
	}




	return 1;



}