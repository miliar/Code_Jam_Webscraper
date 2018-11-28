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
int pl(int n){
	int sqn = n;  
    int i=0; 
    int ncount=1;  
    for(i=10;i<1000000; i*=10 ){  
        if( 0==sqn/i )break;  
        ncount++;  
    }  
      
    int num[10]={0};  
    int j;  
    for(i=0;i<ncount;i++){  
        int mi=1;  
        for(j=0;j<ncount-1-i;j++) mi *=10;  
        num[i] = sqn/mi;  
        sqn = sqn%mi;  
    }  
      
      
      
    int start=0,end=ncount-1,flag=0;  
    while(start <= ncount/2){  
        if(num[start++]!=num[end--]){  
            flag=1;  
            break;  
        }  
    }  
    return 1-flag;
}

int sq(int n){
	int gi=n%10;
	if(gi!=0&&gi!=1&&gi!=4&&gi!=5&&gi!=5&&gi!=9)return 0;
	else{
		for(int i=1;i*i<=n;i++){
			if(i*i==n)return 1;
		}
		return 0;
	}
}
int main(){  
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    FORD(ti,1,t){
    	int a,b;
    	cin>>a>>b;
    	int op=0;
    	FORD(i,a,b){
	    	if(pl(i)&&sq(i)){
	    		op++;
	    		//printf("%d\n",i);
	    	}
	    }
	    printf("Case #%d: %d\n",ti,op);
    }
    return 0;    
}
