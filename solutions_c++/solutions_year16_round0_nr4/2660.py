# include <bits/stdc++.h>
using namespace std;
long long pow(int a, int b)
{
	long long x=1,y=a; 
	while(b > 0)
	{
		if(b%2 == 1)
		{
			x=(x*y);
		}
		y = (y*y);
		b /= 2;
	}
	return x;
}
int main()
{
freopen("input.txt","r", stdin);
freopen("out.txt", "w", stdout);
int t,i,j,c,k,s;
cin>>t;
for(j=1;j<=t;j++)
{
	printf("Case #%d: ",j);
cin>>k>>c>>s;long long int p=1;
long long int diff=pow(k,c-1);
for(i=0;i<k;i++)
{
	printf("%lld ",p);p+=diff;
}
printf("\n");
}
return 0;
}