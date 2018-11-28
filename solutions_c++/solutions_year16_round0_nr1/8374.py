#include <bits/stdc++.h>
using namespace std;


void digits(unsigned long long int ,unsigned long long int);
int check(unsigned long long int );

void digits(unsigned long long int val,unsigned long long int a[])
{
	while(val!=0)
	{
		a[val%10]=1;
		val=val/10;
	}
}

int check(unsigned long long int a[])
    {
    for(int i=0;i<10;i++)
        {
        if(a[i]==0)
            return 1;
        }
    return 0;
}

int main() {
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("2.txt","w",stdout);
	unsigned long long int t;
	cin>>t;
    int c=1;
	while(t--)
	{
		unsigned long long int n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<c++<<": INSOMNIA"<<endl;
		}
		else
		{
            unsigned long long int k=n,a[10]={0};
			for(unsigned long long int i=0;i<100;i++)
			{
				digits(k,a);
				if(check(a))
					k=(i+1)*n;
				else
					break;
			}
			cout<<"Case #"<<c++<<": "<<k<<endl;
		}
	}
	
	return 0;
}
