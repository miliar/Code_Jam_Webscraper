#include<bits/stdc++.h>
#define md 1000000007
#define ll long long
#define gc getchar//_unlocked    
#define limit 50 
using namespace std;
int a[100010];
int main(){
	
	int t,n,m;
	scanf("%d",&t);
	
	for(int k=1;k<=t;k++){
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>a[i];
		printf("Case #%d: ",k);
		int mn=0,mx=0;
		for(int i=0;i<n-1;i++)
		{	mx=max(mx,a[i]-a[i+1]);
	if(a[i+1]<a[i])
		mn+=a[i]-a[i+1];}
	int tot=0;
	int rem=0;
	for(int i=0;i<n-1;i++){
		tot+=min(mx,a[i]);
	}
		printf("%d %d\n",mn,tot);
		
	}
	
	return 0;
}