/*Code By Aquariuslt*/  
#include<iostream>  
#include<string>  
#include<algorithm>  
#include<queue>  
#include<stack>  
#include<vector>  
#include<deque>  
#include<set>  
#include<list>  
#include<map>  
#include<iterator>  
#include<numeric>  
#include<memory>  
#include<utility>  
#include<stdio.h>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)    
#define FORD(i,a,b) for(int i=(a);i<=(b);i++)    
#define REP(i,b) FOR(i,0,b)    
  
typedef long long ll;  
using namespace std;  
int lawn[101][101];
//x,y×ø±ê,n,m±ß½ç 
int check(int x,int y,int n,int m){
	int xflag=1,yflag=1;
	REP(i,n){
		if(lawn[i][y]>lawn[x][y])yflag=0;
	}
	REP(i,m){
		if(lawn[x][i]>lawn[x][y])xflag=0;
	}
	if(xflag==0&&yflag==0)return 0;
	return 1;
}
int main(){  
	freopen("B-large.in","r",stdin);
	freopen("loutput.txt","w",stdout);
    int t;
    cin>>t;
    FORD(ti,1,t){
    	int n,m;
    	cin>>n>>m;
    	REP(i,n){
	    	REP(j,m){
	    		cin>>lawn[i][j];
	    	}
	    }
	    int flag=1;
	    REP(i,n){
    		REP(j,m){
		    	if(!check(i,j,n,m)){
		    		flag=0;
		    		break;
		    	}
		    }
    	}
    	printf("Case #%d: ",ti);
    	if(flag==1)printf("YES\n");
    	else printf("NO\n");
    }
    return 0;    
}
