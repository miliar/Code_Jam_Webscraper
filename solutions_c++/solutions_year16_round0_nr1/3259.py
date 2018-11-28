# include <bits/stdc++.h>
using namespace std;
int main()
{
freopen("input.txt","r", stdin);
freopen("out.txt", "w", stdout);
int t,i,j,n,m,m1;
cin>>t;
for(j=1;j<=t;j++)
{
	cin>>n;
	if(n==0)
	{
		printf("Case #%d: INSOMNIA\n",j);
		continue;
	}
	set <int> s;
	int k=1;
	while(s.size()!=10)
	{
		m=n;m=m*k;k++;m1=m;
          while(m>0)
          {
             s.insert(m%10);
              m/=10; 
          }
	}
printf("Case #%d: %d\n",j,m1);
	}
return 0;
}