#include <bits/stdc++.h>
using namespace std;
map<int,int> M;
int main()
{
FILE *ip,*op;
ip=fopen("testcase1.in","r");
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
long long t;
fscanf(ip,"%lld",&t);
long long l;
while(t--)
{ M.clear();
long long int n,k=1;
fscanf(ip,"%lld",&n);
if(n==0)
fprintf(op,"Case #%lld: INSOMNIA\n",k);
else
{  long long temp=n;
while(M.size()!=10)
{ long long  t=n;
temp=k*n;
while(temp!=0)
{
	M[temp%10];
	temp/=10;
}
k++;	
}

fprintf(op,"Case #%lld: %lld\n",l,(n*(k-1)));	 
}
l++;
}
}
