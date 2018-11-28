#include<stdio.h>
#include<map>
#include<set>
#include<vector>
#include<iostream>
#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>
#include<math.h>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#define For(i,s,e) for(i=s;i<e;i++)
#define ss(a) scanf("%s",a)
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define sf(a) scanf("%f",&a)
#define sd(a) scanf("%lf",&a)
#define ps(a) printf("%s\n",a)
#define pi(a) printf("%d\n",a)
#define pl(a) printf("%lld\n",a)
#define pd(a) printf("%lf\n",a)
#define LL long long
#define MOD 1000000

using namespace std;
 
int main() {
	int t,r1,r2,i,j,a[4],b[4],count,ans,x,k=1;
	si(t);
	while(t--)
	{
		//cout<<t;
		si(r1);
		for(i=0;i<=3;i++)
			for(j=0;j<=3;j++)
			{
				if(i==r1-1)
				si(a[j]);
				else
				si(x);
			}
		si(r2);
		for(i=0;i<=3;i++)
			for(j=0;j<=3;j++){
			if(i==r2-1)
				si(b[j]);
				else si(x);}
 
		count=0;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		if(a[i]==b[j])
		{
			count++;
			ans=a[i];
		}
		if(count==0)
		cout<<"Case #"<<k++<<": "<<"Volunteer cheated!\n";
		else if(count==1)
		cout<<"Case #"<<k++<<": "<<ans<<"\n";
		else
		cout<<"Case #"<<k++<<": "<<"Bad magician!\n";
	}
	return 0;
}

