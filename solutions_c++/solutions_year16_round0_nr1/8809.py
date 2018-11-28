#include<bits/stdc++.h>
using namespace std;

set<int> s;

void setDigit( int x)
{
	int tmp;
	while(x>0)
	{
		tmp=x%10;
		s.insert(tmp);
		x/=10;		
	}	
}
int main()
{
	int t,k,i;
	long long n,tmp,res,gen;
	scanf("%d",&t);
	k=1;
	while(t--)
	{
		s.clear();
		scanf("%lld",&n);
		tmp=n;
		i=1;
		if(n==0)
			printf("Case #%d: INSOMNIA\n",k);
		else
		{
			while(true)
			{
				gen=tmp*i;
				setDigit(gen);
				if(s.size()==10)
				{
					//cout<<"size :"<<s.size()<<endl;
					res=gen;
					printf("Case #%d: %lld\n",k,res);
					break;
				}
				i++;
			}
		}
		++k;
	}
}
