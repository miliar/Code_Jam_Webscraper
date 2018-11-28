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

void judge(){
	double rat=2,c,f,x,time=0,to=0;
	scanf("%lf%lf%lf",&c,&f,&x);
	while(x-to>c){
		time+=c/rat;
		to+=c;
		if((x-to)/rat<(x+c-to)/(rat+f))break;
		to-=c;
		rat+=f;
	}
	time+=(x-to)/rat;
	printf("%.7lf",time);

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