#include<bits/stdc++.h>
using namespace std;

typedef long long int LL;
int main()
{
	ifstream cin("Q1L.in");
	ofstream cout("Q1LA.txt");	
	int t,i,j,k,l,cnt,ind=1;
	LL m,n,a,b,c,d;
	cin>>t;
	while(t--)
	{
		cin>>n;
		cout<<"Case #"<<ind++<<": ";
		if(n==0)
		cout<<"INSOMNIA"<<endl;
		else
		{
			bool check[10];
			memset(check,false,sizeof(check));
			cnt=0,i=0;
			while(cnt<10)
			{
				i++;
				a=1LL*i*n;
				
				while(a)
				{
					k=a%10;
					if(!check[k])
					{
						check[k]=true;
						cnt++;
					}
					a=a/10LL;
				}
				
			}
			cout<<1LL*i*n<<endl;
			
		}
	}
	
}
