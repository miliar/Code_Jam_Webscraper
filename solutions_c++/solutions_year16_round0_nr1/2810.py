#include <bits/stdc++.h>
using namespace std;

#define ll long long 

int visited[10];
int counter;

void mark(ll n){
	while(n){
		if(visited[n%10]==0){
			counter++;
			visited[n%10]=1;
		}
		n/=10;
	}
}

int main()
{
     freopen ("A-large.in","r",stdin); 
     freopen ("A-large.out","w",stdout); 
     ll i,j,n,t,m;
     scanf("%lld",&t);
     for(int casenum=1;casenum<=t;casenum++){
     	for(i=0;i<10;i++)
     		visited[i]=0;
     	counter=0;
     	scanf("%lld",&n);
     	m=n;
     	for(i=0;;i++){
     		mark(n);
     		if(counter==10){
     			printf("Case #%d: %lld\n",casenum,n);
     			break;
     		}
     		if(i==1000000){
     			printf("Case #%d: INSOMNIA\n",casenum);
     			break;
     		}
     		n+=m;
     	}
     }

	return 0;
}  