#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int A[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
int tr(int i,int j)
{
    int sgn=1;
    if ((i<0 && j>0) || (i>0 && j<0))
	sgn=-1;
    if (i<0)
	i=-i;
    if (j<0)
	j=-j;
    return (sgn*A[i-1][j-1]);
}
int find (int k, int st, int len, int temp[], int b)
{
    int out=-1;
    for (int i=st;i<len;i++)
    {
	if (tr(b,temp[i])==k)
	{
	    out=i;
	    break;
	}
    }
    return out;
}
int debug = 0;
int findfirst (int k, int st, int len, int arr[], int *outj)
{
    int out=-1;
    *outj = 1;
    for (int i=st;i<len;i++)
    {
	*outj=tr(*outj,arr[i]);
	if (debug)
	    printf("\nfindfirst out %d i %d k %d",*outj,i,k);
	if (*outj==k)
	{
	    out=i;
	    break;
	}

    }
    return out;
}
int main()
{
    int T,arr[10100],temp[10100];
    string inp;
    int l,x;
    cin>>T;
    for (int i=0;i<T;i++)
    {
	cin>>l>>x>>inp;
	for (int j=0;j<l;j++)
	{
	    if (inp[j]=='i')
		arr[j]=2;
	    else if (inp[j]=='j')
		arr[j]=3;
	    else
		arr[j]=4;
	}
	temp[0]=arr[0];
	for (int j=1;j<l;j++)
	{
	    temp[j]=tr(temp[j-1],arr[j]);

	}
	int b=1;
	int indi=find(2,0,l,temp,b);
	for (int j=0;j<4 && indi==-1;j++)
	{
	    b=tr(b,temp[l-1]);
	    indi=find(2,0,l,temp,b);
	    x=x-1;
	}
	if (indi==-1 )
	{
	    printf("Case #%d: NO\n",i+1);
	    continue;
	}
	if (indi==l-1)
	{
	    indi=-1;
	    x=x-1;
	}
	if (debug)
	    printf("\n%d %d\n",indi,x);
	b=1;
	int outj;
	int indj=findfirst(3,indi+1,l,arr,&outj);
	b=outj;
	if (debug)
	    printf("\nb %d\n",b);
	for (int j=0;j<4 && indj==-1;j++)
	{
	    indj=find(3,0,l,temp,b);
	    b=tr(b,temp[l-1]);
	    x=x-1;
	}
	if (indj==-1 || x<0)
	{
	    printf("Case #%d: NO\n",i+1);
	    continue;
	}
	if (indj==l-1)
	{
	    indj=-1;
	    x=x-1;
	}
	if (debug)
	    printf("\nindj %d  x %d\n",indj,x);
	int outk;
	outk=1;
	for (int j=indj+1;j<l;j++)
	{
	    outk=tr(outk,arr[j]);
	}
	x=x-1;
	if (x<0)
	{
	    printf("Case #%d: NO\n",i+1);
	}
	else
	{
	    for (int j=x;j>0;j--)
		outk=tr(outk,temp[l-1]);
	    if (outk==4)
		printf("Case #%d: YES\n",i+1);
	    else
		printf("Case #%d: NO\n",i+1);
	}

    }
    return 0;
}

