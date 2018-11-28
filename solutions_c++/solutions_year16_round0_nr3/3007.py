#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("q3_test1.out","w",stdout);
	int t;
	cin>>t;
	while(t--)
	{
		int n,j;
		cin>>n>>j;
		cout<<"Case #1"<<": "<<endl;
		long long st,en;
		st=pow(2,n-1)+1;
		en=pow(2,n)-1;
		while(j--)
		{
			int a[n];
			long long d[9];
			for(int i=0;i<9;i++)
			{
				d[i]=0;
			}
			int f=0;
			long long cy=st;
			while(f!=1)
			{
				cy=st;
				for(int i=0;i<n;i++)
				{
					a[i]=cy%2;
					cy=cy/2;
				}
				if((a[0]!=a[n-1])||(a[0]!=1))
				{
					st++;
					continue;
				}
				int fl=0;
				for(int i=2;i<=10;i++)
				{
					double pw = n/2;
					long long ftc=pow(i,pw);
					long long ck = 2;
					long long num=0;
					fl=0;
					while(ck<=ftc)
					{
						num=0;
						for(int j=n-1;j>=0;j--)
						{
							num=num*i;
							//num=num%ck;
							num=num+a[j];
						}
						if(num%ck==0)
						{
							//cout<<num<<"  ck = "<<ck<<endl;
							d[i-2]=ck;
							fl=1;
							break;
						}
						ck++;
					}
					if(fl==0)
					{
						break;
					}
				}
				if(fl==0)
				{
					st++;
				}
				else
				{
					f=1;
					for(int i=n-1;i>=0;i--)
					{
						cout<<a[i];
					}
					for(int i=0;i<9;i++)
					{
						cout<<" "<<d[i];
					}
					cout<<endl;
					st++;
				}
			}
		}
	}
	return 0;
}
