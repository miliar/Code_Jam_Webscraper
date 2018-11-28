/*----Ratnesh----*/
#include<bits/stdc++.h>
#include<set>
using namespace std;

set<int>s;
int main()
{
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int count=1;
	while(t--)
	{
		s.clear();
		int n;
		cin>>n;
		int sum=0,r;
		if(n==0)
		{
			cout<<"Case #"<<count<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
			int i=1,flag=0;
			while(i<=100)
			{
				sum=n*i;
				int temp=sum;
				while(sum>0)
				{
					r=sum%10;
					s.insert(r);
					sum=sum/10;
					if(s.size()==10)
					{
						cout<<"Case #"<<count<<": "<<temp<<endl;
						flag=1;
						break;
					}
				}
				if(flag)
					break;
				i++; 
				if(i>100)
				{
					cout<<"Case #"<<count<<":"<< "INSOMNIA"<<endl;
					break;
				}
			}
		}
		count++;
	}
	return 0;
}

