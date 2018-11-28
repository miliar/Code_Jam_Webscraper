#include <iostream>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#define N 110

using namespace std;

string a[N];
string s;
int b[N][N];
int c[N];

int main()
{
	int n,m;
	int T;
	int i,j,k;
	int l,ls;
	int mid;
	int sum;
	cin>>m;
	T=m;
	while(m--)
	{
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		l=a[0].length();
		s.clear();
		s.push_back(a[0][0]);
		b[0][0]=1;
		for(i=1;i<l;i++)
		{
			if(a[0][i]!=s[s.length()-1])
			{
				s.push_back(a[0][i]);
				b[0][s.length()-1]=1;
			}
			else
			{
				b[0][s.length()-1]++;
			}
		}
		
		ls=s.length();
		//cout<<s<<endl;

		int flag;
		//cout<<endl;
		cout<<"Case #"<<T-m<<": ";
		for(i=1;i<n;i++)
		{
			l=a[i].length();
			for(j=0,k=0;j<ls;j++)
			{
				b[i][j]=0;
			}
			for(j=0,k=0,flag=1;j<l;j++)
			{
				if(k>=ls)
				{
					flag=0;
					break;
				}
				if(a[i][j]!=s[k])
				{
					if(!b[i][k])
					{
						flag=0;
						break;
					}
					else
					{
						k++;
						j--;
					}
				}
				else
				{
					b[i][k]++;
				}
			}
			if(!flag||k<ls-1)
			{
				//cout<<flag<<endl;
				break;
			}

		}
		if(i<n)
		{
			cout<<"Fegla Won"<<endl;
			continue;
		}
		mid=n/2;
		for(i=0,sum=0;i<ls;i++)
		{
			for(j=0;j<n;j++)
			{
				c[j]=b[j][i];
			}
			sort(c,c+n);
			for(j=0;j<n;j++)
			{
				sum=sum+abs(c[j]-c[mid]);
			}

		}
		/*for(i=0,j=0,k=1;i<l;i++)
		{
			if(j>=ls)
			{
				k=0;
				break;
			}
			if(a[1][i]!=s[j])
			{
				//cout<<i<<" "<<j<<" "<<a[1][i]<<" ";

				if(!b[1][j])
				{
					k=0;
					//cout<<"b"<<endl;
					break;
				}
				else
				{
					j++;
					i--;
					//cout<<"c"<<endl;
					continue;
				}
				
			}
			else
			{
				//cout<<i<<" "<<j<<" "<<a[1][i]<<endl;
				b[1][j]++;
			}
		}*/
		
		
		
		cout<<sum<<endl;


	}
	return 0;
}