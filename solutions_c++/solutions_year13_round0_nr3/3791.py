									/*	In the name of God	*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;

bool ispal(char s[]){
	int i,j,len=strlen(s);
	for (i=0,j=len-1;i<j;i++,j--)
		if (s[i]!=s[j])return 0;
	return 1;
}
ll p[10001],list[10001],np=0;
char t[1001],s[1001];
int main(){
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);	
	int tc,ti,j;
	ll a,b,i;
	rep(j,10000){
		sprintf(t,"%d",j+1);
		sprintf(t,"%s%s",t,strrev(t));
		sscanf(t,"%lld",&a);
		sprintf(s,"%lld",a*a);
		if (ispal(s)){
			//list[np]=a;
			p[np++]=a*a;
		}
		sprintf(t,"%d",j+1);
		sprintf(t,"%s%s",t,strrev(t+1));
		sscanf(t,"%lld",&a);
		sprintf(s,"%lld",a*a);
		if (ispal(s)){
			//list[np]=a;
			p[np++]=a*a;
		}
	}
	sort(p,p+np);
	//sort(list,list+np);
	//rep(i,np)
	//	printf("%lld %lld\n",list[i],p[i]);
	
	scanf("%d",&tc);

	rep(ti,tc){
		int r=0;
		scanf("%lld %lld",&a,&b);
		printf("Case #%d: %d\n",ti+1,upper_bound(p,p+np,b)-lower_bound(p,p+np,a));
	}
	
	return 0;
}