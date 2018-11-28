#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

long long a[10000011];
int N=10000001;
int n=0;

char s[150];
bool check(long long x)
{
		sprintf(s,"%lld",x);
		for (int i=0,j=strlen(s)-1;i<j;i++,j--)
				if (s[i]!=s[j])
						return false;
		return true;
}

int main()
{
	long long t;
		for (int i=1;i<=N;i++)
		{
			t=i;
			t*=i;
				if (check(i)&&check(t))
						a[n++]=t;
		}
		int T;
		cin>>T;
		for (int cas=1;cas<=T;cas++)
		{
				long long A,B;
				cin>>A>>B;
				long long l,r,m;
				l=0;
				r=n-1;
				//first >= A
				while (l<r)
				{
						m=l+(r-l)/2;
						if (a[m]>=A)
								r=m;
						else
								l=m+1;
				}
				long long L=l;
				l=0;
				r=n-1;
				//first > B
				while (l<r)
				{
						m=l+(r-l)/2;
						if (a[m]>B)
								r=m;
						else
								l=m+1;
				}
				cout<<"Case #"<<cas<<": "<<l-L<<endl;
		}
}
