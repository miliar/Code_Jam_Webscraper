/*   ARSHEYA RAJ   */

#include <iostream>
#include <bits/c++io.h>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <exception>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iterator>
 
#define ll long long int
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) a>b?b:a
#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR_X(i,x,n) for(i=x;i<n;i++)
#define BACK(i,n) for(i=n;i>=0;i--)
#define BACK_X(i,n,x) for(i=n;i>=x;i--)
#define fill(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define pp pair<int,int>
#define mod 1000000007

using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	ll t=100,n,x,a[10],r,ans=0,k=1,counter=1,i;
	for(i=0;i<=9;i++){
		a[i]=0;
	}
	scanf("%lld",&t);
	while(t--){
		scanf("%lld",&n);
		x=n;
		if(n==0){
			printf("Case #%lld: INSOMNIA\n",counter);
			counter++;
			continue;
		}
		else{
			while(k<1000005){
				//printf("k=%lld\n x=%lld\n",k,x);
			while(x>=1){
				r=x%10;
				x=x/10;
				//printf("r=%lld ",r);
				if(r==0){
					a[0]=1;
				}
				else if(r==1){
					a[1]=1;
				}
				else if(r==2){
					a[2]=1;
				}
				else if(r==3){
					a[3]=1;
				}
				else if(r==4){
					a[4]=1;
				}
				else if(r==5){
					a[5]=1;
				}
				else if(r==6){
					a[6]=1;
				}
				else if(r==7){
					a[7]=1;
				}
				else if(r==8){
					a[8]=1;
				}
				else if(r==9){
					a[9]=1;
				}
			}
			/*printf("\n");
				for(i=0;i<=9;i++){
					printf("%lld ",a[i]);
				}		
				printf("\n");*/
				k++;
				x=k*n;
				if((a[0]==1) && (a[1]==1) && (a[2]==1) && (a[3]==1) && (a[4]==1) && (a[5]==1) && (a[6]==1) && (a[7]==1) && (a[8]==1) && (a[9]==1)){
				ans=(k-1)*n;
				break;
				}
				if(k==100000){
					ans=0;
					break;
				}
			}
		}
		if(ans==0){
			printf("Case #%lld: INSOMNIA\n",counter);
		}
		else{
			printf("Case #%lld: %lld\n",counter,ans);
		}
		counter++;
		ans=0;
		k=1;
		for(i=0;i<=9;i++){
		a[i]=0;
		}
	}
return 0;
}