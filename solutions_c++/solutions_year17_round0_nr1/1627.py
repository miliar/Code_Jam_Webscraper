/*
Shubham Gupta
=============

MNNIT CSE 3rd year
==================
*/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
char str[2000];
ll k;
void modify(ll j){
	for(ll i=0;i<k;i++){
		if(str[i+j]=='+')
			str[i+j]='-';
		else
			str[i+j]='+';
	}
}
ll valid(void){
	for(ll i=0;str[i];i++){
		if(str[i]=='-')
			return 1;
	}
	return 0;
}
int main()
{
ll t;
scanf("%lld",&t);
for(ll i=1;i<=t;i++){
	ll ans=0,possible=0;
	scanf("%s",str);
	scanf("%lld",&k);
	ll n=strlen(str);
	for(ll j=0;j<=n-k;j++){
		if(str[j]=='-')
			{
				modify(j);
				ans++;
				//printf("%s\n",str);
			}
	}
	possible=valid();
	if(possible==0)
		printf("Case #%lld: %lld\n",i,ans);
	else
		printf("Case #%lld: IMPOSSIBLE\n",i);
	//printf("%s\n",str);
}
return 0;
}