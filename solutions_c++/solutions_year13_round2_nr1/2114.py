#include<iostream>
#include<fstream>
using namespace std;
int min(int a,int b)
{
	if(a<=b)return a;return b;
}
void merge(int a[],int p,int q,int r)
{
	int c[10];
	int i=p;
	int j=q+1;
	int k=p;
	while((i<=q)&&(j<=r))
	{
		if(a[i]<a[j])
		{
    		c[k]=a[i];
      		i=i+1;
     		k=k+1;
		}
		else
		{
     		c[k]=a[j];
      		j=j+1;
      		k=k+1;
		}
	}
	while(i<=q)
	{
     	c[k] =a[i];
     	i=i+1;
     	k=k+1;
	}
	while(j<=r)
	{
     	c[k]=a[j];
     	j=j+1;
     	k=k+1;
	}
	int l=p;
	while(l<=r)
	{
		a[l]=c[l];
		l=l+1;
	}
}
void mergesort(int a[],int p,int r)
{
    if(p<r)
    {
         int q=(p+r)/2;
         mergesort(a,p,q);
         mergesort(a,q+1,r) ;
         merge(a,p,q,r);
    }
}
int f1(int a,int n,int p[100],int s)
{
	if(s>=n)return 0;
	else if(a>p[s])
		return f1(a+p[s],n,p,s+1);
	else if(a!=1)
		return 1+min(f1(a+a-1,n,p,s),f1(a,n,p,s+1));
	else
		return n;
}
int main()
{
	int t,i,j,k,a,n,m[100];
	ifstream f("1.in");
	ofstream g("1.out");
	f>>t;
	for(k=1;k<=t;k++)
	{
		f>>a>>n;
		for(i=0;i<n;i++)
		f>>m[i];
		mergesort(m,0,n-1);
		//for(i=0;i<n;i++)
		//cout<<m[i]<<" ";
		int j=f1(a,n,m,0);
		g<<"Case #"<<k<<": "<<j<<endl;
	}
	return 0;
}
