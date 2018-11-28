#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
 	freopen("D-small-attempt0.out","w",stdout);
    long long T,Case=1,K,C,S,i=1,a=-2,b=0,c=0,d=0;
    cin>>T;
    while(T--)
    {
    	cin>>K>>C>>S;
    	if(C==1)
		{
    		if(S>=K)
			{
			cout<<"Case #"<<Case<<": ";
			while(K--){cout<<i++<<' ';}
			cout<<endl;
			}
    		else cout<<"Case #"<<Case<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			if(((K+1)/2)<=S&&K%2==0)
			{
				cout<<"Case #"<<Case<<": ";
				b=(K+1)/2;
				while(b--)
				{
					a+=2;
					c+=2;
					d=a*K+c;
					cout<<d<<' ';
				}
				cout<<endl;
			}
			else if(((K+1)/2)<=S&&K%2==1)
			{
				cout<<"Case #"<<Case<<": ";
				b=((K+1)/2)-1;
				while(b--)
				{
					a+=2;
					c+=2;
					d=a*K+c;
					cout<<d<<' ';
				}
				a+=2;
				c+=2;
				d=a*K+c-1;
				cout<<d<<' '<<endl;
			}
			else cout<<"Case #"<<Case<<": "<<"IMPOSSIBLE"<<endl;
		}
    	Case++;
    	a=-2,b=0,c=0,d=0,i=1;
	}
}
