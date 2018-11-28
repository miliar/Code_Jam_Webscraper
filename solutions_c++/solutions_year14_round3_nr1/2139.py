#include<iostream>
#include<cstdio>
#include<fstream>
#define EPS 1e-9
using namespace std;
typedef long long int LL;
LL gcd(LL a, LL b)
{
	if(a==0)return b;
	return gcd(b%a,a);
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("aa.out","w",stdout);
	int t,in; 
	for(in =1, scanf("%d",&t);t--;in++)
	{
		long long int p,q;
		scanf("%lld/%lld",&p,&q);
		LL g = gcd(p,q);
		p = p/g;
		q = q/g;
		double n = p/(double)q;
		//cout <<p <<" "<< q << " "<< n << " ";
		int j =0,ans=0;
		while(j<41)
		{
			double y= 2*n;j++;
			if(y-1.0<EPS && 1-y <EPS)break;
			else if(y-1.0>EPS)
				{n= y-1.0;ans  = (ans == 0)?j:ans;}
			else if(1.0-y>EPS)n =y;
		}
		printf("Case #%d: ",in);
		if(j==41)cout <<"IMPOSSIBLE\n";
		else if(ans<j && ans >0)cout << ans << endl;
		else cout << j<<endl;
	}
}
/*

5
1/2
3/4
1/4
2/23
123/31488
*/