
#include<cstdio>
#include<cmath>
#include<cstring>
using namespace std;
bool pln(int i)
{char sr[100];
		sprintf(sr,"%d",i);
		int l=strlen(sr);
	 bool	r=1;
		for(int k=0;k<(strlen(sr)+1)/2;k++)
		{
		if(sr[k]!=sr[l-1])
			r=0;
		l--;
		}
		if(r)
			return true;
		return false;
}

int main()
{ FILE*fout=fopen("output.txt","w"); 
FILE*fin=fopen("input.txt","r"); 	
int m,n,l,d;
	fscanf(fin,"%d ",&d);
	for(int k=0;k<d;k++)
	{fscanf(fin,"%d%d",&n,&m);
	int a=n,b=m, y=0;
	if(n>m)
		a=m,b=n;
	for(int i=a;i<=b;i++)
		{	bool z=pln(i);
	bool o=false;
	if((int)(sqrt(i))*(int)(sqrt(i))==i)
	o=pln(sqrt(i));

	if(o&&z)
		y++;
	}
	fprintf(fout,"Case #%d: %d\n",k+1,y);
	}

	
	
return 0;
}