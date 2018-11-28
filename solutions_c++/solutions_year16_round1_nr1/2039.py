#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int l,t,n,i,j,k;
	FILE *ptr,*ptr1;
	char s[1009];
	string ss;
	ptr=fopen("A1-large.in","r+");
	ptr1=fopen("A1-large2.in","w+");
	fscanf(ptr,"%lld",&t);
	for(j=1;j<=t;j++)
	{
		fscanf(ptr,"%s",&s);
		long long int f=0;
		long long int c=0;
		for(i=0;s[i]!='\0';i++)
		{
			if(i==0||s[i]<ss[0])
			ss.insert(ss.end(),s[i]);
			else
			ss.insert(ss.begin(),s[i]);
			
		}
		fprintf(ptr1,"Case #%lld: %s\n",j,ss.c_str());
		ss.clear();
	}
	fclose(ptr);
	fclose(ptr1);
	return 0;
}
