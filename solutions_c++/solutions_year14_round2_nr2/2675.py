/* Sahil Sondhi : Don't check my solutions STALKER!*/
 

#include <iostream>
#include<vector>
#include<cmath>
#include <iomanip>
#include<string>
#include<algorithm>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<list>
#include<map>
#include<cctype>
#include<limits.h>

#define scan(x) scanf("%d",&x)
#define forall(i,x,n) for(int i=x;i<n;i++)
#define forl(i,x,n) for(long i=x;i<n;i++)
#define forequal(i,x,n) for(int i=x;i<=n;i++)
#define scanl(x) scanf("%ld", &x)
#define scanll(x) scanf("%lld", &x)
#define minimum(a,b) (a>=b?b:a)
#define maximum(a,b) (a<=b?b:a)
#define scanfloat(x) scanf("%f", &x)
#define mod 1000000009
#define swap(xxx,yyy) { xxx=xxx+yyy; yyy=xxx-yyy; xxx=xxx-yyy; }
#define MAXARRAY 730000
#define __gcd(a,b) gcd(a,b)
#define LL long long
#define LD long double


using namespace std;



int main()
{
	int t;
	int a,b,k;
	int x,y;
	cin>>t;
	
	for(int p=1;p<=t;p++)
	{
	long count =0;
		cin>>a>>b>>k;
		
		for(int i=0;i<a;i++)
		 for(int j=0;j<b;j++)
			{
				x=i&j;
				//y=j;
				if(x < k)
				{ count++;
		//			cout<<i<<" "<<j<<endl;
				}
			}
	
		cout<<"Case #"<<p<<": "<<count<<endl;
	
	
	}
		
	return 0;


}
