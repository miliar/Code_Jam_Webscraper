#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long int
#define ll long long int
#define MOD 1000000007
/*void scanint(int &x)
{
    register int c = getchar_unlocked();
    x = 0;
    for(;(c<48 || c>57);c = getchar_unlocked());
    for(;c>47 && c<58;c = getchar_unlocked()) {x = (x<<1) + (x<<3) + c - 48;}
}*/
/*typedef struct tree{
	int a,b;
}ar;
bool myf(ar p,ar q){
	return p.b<q.b;
}*/
/*int gcd(int p,int q){
	if(q==0)
		return p;
	return gcd(q,p%q);
}*/
char ar[1002];
int main(){
	int t,cas=1,n,i,ans=0,val;
	scanf("%d",&t);
	while(t--){
		ans=0;
		val=0;
		scanf("%d %s",&n,ar);
		//printf("%s",ar);
		val+=(int)ar[0]-48;
		for(i=1;i<=n;i++){
			if(i>val && (int)ar[i]-48>0){
				ans+=(i-val);
				val+=(i-val);
				val+=(int)ar[i]-48;
				//cout<<ans<<endl;
			}
			else
				val+=(int)ar[i]-48;
		}
		printf("Case #%d: %d\n",cas++,ans);
	}
return 0;}
/*
scanf("%d",&t);
scanint(t);
 */
