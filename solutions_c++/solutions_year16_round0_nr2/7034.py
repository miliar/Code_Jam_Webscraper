#include<bits/stdc++.h>
#include<fstream>
using namespace std;
void flip(int a[],int p)
{
	int l=0;
	while(l<=p)
	{
		int t=a[p];
		a[p]=a[l]^1;
		a[l]=t^1;
		l++;
		p--;
	}
}

int main()
{
	ifstream in("B-large.in");
	ofstream out("output_B_large.txt");
	int t;
	in>>t;
	int m=t;
	while(t--)
	{
		string s;
		in>>s;
		int l=s.length();
		int a[l];
		for(int i=0;i<l;i++)
		{
			if(s[i]=='+')
			a[i]=1;
			else
			a[i]=0;
		}
		/*for(int j=0;j<l;j++)
				cout<<a[j]<<" ";
				cout<<"\n";*/
		int j=0,f=0;
		int count=0;
		for(int i=l-1;i>=0;i--)
		{
			j=0;
			if(a[i]==0)
			{
				while(a[j])
				{
					a[j++]=0;
					f=1;
				}
				if(f)
				{
					count++;
				}
				flip(a,i);
				/*for(int j=0;j<l;j++)
				cout<<a[j]<<" ";
				cout<<"\n";*/
				count++;
			}
		}
		/*cout<<"\n";
		for(int j=0;j<l;j++)
				cout<<a[j]<<" ";
				cout<<"\n";*/
		cout<<"Case #"<<m-t<<": "<<count<<"\n";
		out<<"Case #"<<m-t<<": "<<count<<"\n";
	}
}
