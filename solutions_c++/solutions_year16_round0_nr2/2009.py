#include<bits/stdc++.h>
#include<string>
using namespace std;
char s1[102];
int counts(char a[],int p,int d)
{
	int count=0,u,y,v=0,valid=0,b[102];
	while(a[d]=='+'&&d>=0)
	d--;
	//cout<<d<<endl;
	if(d==-1)
	return 0;
	else
	{
		while(a[p]=='+')
		{
			a[p]='-';
			valid=1;
		    p++;
	    }
	    if(valid==1)
		count++;
		for(u=0;u<=d;u++)
		{
			if(a[u]=='-')
			b[v++]='+';
			else b[v++]='-';
		}
		int p=0;
		while(v>=1)
		{
		  a[p++]=b[v-1];
		  v--;
	    }
		count++;
		//for(int i=0;i<=d;i++)
		//cout<<a[i]<<" "<<"#"<<" " ;
		return count+counts(a,0,d);
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int m=1;m<=t;m++)
	{
	    int count=0;
		scanf("%s",s1);
	//	cout<<s1<<" "<<endl;
		int l=strlen(s1);
	//	cout<<l<<endl;
		int b=counts(s1,0,l-1);
		printf("Case #%d: %d\n",m,b);
	}
	return 0;
}
