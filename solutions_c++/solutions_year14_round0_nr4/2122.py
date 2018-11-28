#include<fstream>
#include<iostream>
using namespace std;
void merge(int low, int mid, int high, double a[])
{
	double b[1005];
	int i=low,j=mid+1,k=low;
	while((i<=mid)&&(j<=high))
	{
		if(a[i]<a[j])
		{
			b[k]=a[i];
			k++;
			i++;
		}
		else
		{
            b[k]=a[j];
			k++;
			j++;
		}
	}
		while(i<=mid)
		{
            b[k]=a[i];
			k++;
			i++;
		}
		while(j<=high)
		{
            b[k]=a[j];
			k++;
			j++;
		}
		for(i=low;i<=high;i++)
		 a[i]=b[i];
}
void mergesort(int low, int high, double a[])
{
	int mid=(low+high)/2;
	if(low<high)
	{
		mergesort(low,mid,a);
		mergesort(mid+1,high,a);
		merge(low,mid,high,a);
	}
}
int min(double a[],int size)
{
	int i=0,pos;
	double m;
	while(a[i]==-1)
		i++;
	pos=i;
	m=a[i];
	for(int k=i;k<size;k++)
	{
		if((a[k]<m)&&(a[k]!=-1))
		{
			m=a[k];
			pos=k;
		}
	}
	return pos;
}
int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	double a[1005],b[1005],n[1005],k[1005],p[1005],q[1005];
	int t,m,size,pn,pk,pn1,pk1,i,j,ck,cn,x,y,z;
	fin>>t;
	for(m=1;m<=t;m++)
	{
		fin>>size;
		for(i=0;i<size;i++)
			fin>>a[i];
		for(i=0;i<size;i++)
			fin>>b[i];
		for(i=0;i<size;i++)
		{
			n[i]=a[i];
			p[i]=a[i];
			k[i]=b[i];
			q[i]=b[i];
		}
		pn=0;pk=0;pn1=0;pk1=0;
		mergesort(0,size-1,n);
		mergesort(0,size-1,k);
		mergesort(0,size-1,p);
		mergesort(0,size-1,q);
		for(i=0;i<size;i++)
		{
			cn=i;
			for(j=size-1;j>=0;j--)
			{
				if((k[j]<n[cn])&&(k[j]!=-1.0))
				{
					break;
				}

			}
			if(j==size-1)
			{
				ck=0;
				while(k[ck]==-1)
					ck++;
			}
			else
			{
				ck=j+1;
				while((k[ck]==-1.0)&&(ck<size))
					ck++;
				if(ck==size)
					ck=min(k,size);
			}
			if(n[cn]>k[ck])
				pn++;
			else
				pk++;
			n[cn]=-1.0;
			k[ck]=-1.0;
		}
		for(x=0;x<size;x++)
		{
			y=0;z=size-1;
			while(q[y]==-1.0)
				y++;
			if(q[y]<p[x])
			{
				pn1++;
				q[y]=-1.0;p[x]=-1.0;
			}
			else
			{
				while(q[z]==-1)
					z--;
				pk1++;
				p[x]=-1.0;q[z]=-1.0;
			}
		}
		fout<<"Case #"<<m<<": "<<pn1<<" "<<pn<<"\n";
	}
}