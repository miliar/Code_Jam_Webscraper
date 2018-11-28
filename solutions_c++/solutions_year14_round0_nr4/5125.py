#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;
char s[3000000]="\0";

int main()
{
	int n,m,i;
	//ios_base::sync_with_stdio(false);
	//cin >> n >> m;
	scanf("%d %d",&n,&m);
	//s.clear();
	if(n>m+1 || m>2+2*n)
	{
		//cout << -1 << endl;
		printf("-1\n");
		return 0;
	}
	if(n>m)
	{
		for(i=0;i<m;i++)
		{
			s[i*2] = '0';
			s[i*2+1] = '1';
		}
		s[i*2]='0';
		s[i*2+1]='\0';
		//printf("%s\n",s);
		//cout << s << endl;
		puts(s);
		return 0;
	}
	int r,rr;
	if(m>=2*n)
		{r=n;
		}
	else{

		r=m%n;

	}
	rr=n-r;
	for(i=0;i<r;i++)
	{
		//s = s + "110";
		s[i*3]=s[i*3+1]='1';
		s[i*3+2]='0';
	}
	i=r*3;
	for(int j=0;j<rr;j++)
	{
			s[i] ='1';s[i+1]='0';
			i+=2;
	}
	if(m==2*n+1)
		s[i++] = '1';
	else if(m==2+2*n)
	{
		s[i]=s[i+1]='1';
		i+=2;
	}
	s[i]='\0';
	//cout << s<<endl;
	puts(s);
	return 0;
}
