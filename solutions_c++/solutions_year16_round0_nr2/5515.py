#include <bits/stdc++.h>
using namespace std;
int main()
{ 
 long long t,m;
FILE *ip,*op;
ip=fopen("input.in","r");
	if(ip==NULL)
	{
		cout<<"ERROR!!";
		exit(0);
	}
	op=fopen("output1.in","w");
	if(op==NULL)
	{
		cout<<"ERROR!!";
		exit(0);
	}
fscanf(ip,"%lld",&t);
//getchar();
 m=1; 
while(t--)
{
 int c=0; char ch[1000],str[1000];char a;int k=0;
 fscanf(ip,"%s",str);
// cout<<ch<<endl;
 
//while((a=getchar())!='\n')
for(int i=0;i<strlen(str);i++) 
ch[k++]=str[i];
for(int i=0;i<k-1;i++)
{  if(ch[i]!=ch[i+1])
{  char d= ch[i+1];c++;
	for(int l=0;l<=i;l++)
	{
	ch[l]=d;	}
	

}
//for(int j=0;j<k;j++)cout<<ch[j];
//cout<<endl;
}

  if(ch[0]=='-')
c++;
	
fprintf(op,"Case #%lld: %lld\n",m,c);
m++;
}

}
