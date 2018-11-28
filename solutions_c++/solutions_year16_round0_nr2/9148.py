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
	int t=105,n=105,a[n],i,ans=0,p,q,temp,totans=0,counter=1;
	string s;
	scanf("%d",&t);
	while(t--){
		cin>>s;
		n=s.size();
		//printf("size=%d\n",n);
		for(i=1;i<=n;i++){
			a[i]=0;
		}
		for(i=0;i<n;i++){
			if(s.at(i)=='+'){
				a[i+1]=1;
			}
			else if(s.at(i)=='-'){
				a[i+1]=0;
			}
		}
		/*for(i=1;i<=n;i++){
			printf("%d ",a[i]);
		}
		printf("\n");*/
		if(n==1){
			if(a[1]==0){
			printf("Case #%d: 1\n",counter);
			counter++;
			continue;
			}
			else{
			printf("Case #%d: 0\n",counter);
			counter++;
			continue;
			}
		}
		i=1;
		while(i<n){
			if(a[i]==a[i+1]){
				i++;
				continue;
			}
			else{
				if((i%2)==0){
					for(p=1,q=i;p<=(i/2),q>=(i/2);p++,q--){
						temp=a[p];
						a[p]=a[q];
						a[q]=temp;
					}
				}
				else{
					for(p=1,q=i;p<=(i/2),q>(i/2)+1;p++,q--){
						temp=a[p];
						a[p]=a[q];
						a[q]=temp;
					}
				}
				for(p=1;p<=i;p++){
					if(a[p]==0){
						a[p]=1;
					}
					else if(a[p]==1){
						a[p]=0;
					}
				}
				/*for(i=1;i<=n;i++){
					printf("%d ",a[i]);
				}
				printf("\n");*/
				ans++;
				i=1;
			}
		}
		if(a[1]==0){
			totans=ans+1;
		}
		else{
			totans=ans;
		}
		printf("Case #%d: %d\n",counter,totans);
		ans=0;
		totans=0;
		counter++;
	}
return 0;
}