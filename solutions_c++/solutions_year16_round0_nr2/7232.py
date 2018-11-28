#include<bits/stdc++.h>
using namespace std;
typedef long long int des;
des hash[10];
int main()
{	int t;
	char a[201];
	int counta;
	int i,n;
	int k=1;
	scanf("%d",&t);
	while(t--)
	{	scanf("%s",a);
		counta=0;
		n=strlen(a);
	
		for(i=0;i<n;i++)
		{	if(a[i]=='+'&&(i+1)<n&&a[i+1]=='-')
			{		if(i+2==n)counta+=2;
					else	counta++;
				//i=0;
			}
		else	if(a[i]=='-'&&a[i+1]=='+')
			{	counta++;
				//i=0;
			}
		}
		if(counta==0&&a[0]=='-')counta++;
		else if(a[n-1]=='-'&&a[n-2]=='-')counta++;
		printf("Case #%d: %d\n",k++,counta);
	}
	return 0;
}
	//Case #1: 1
