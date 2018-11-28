#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;


	char h[10],v[1001];
	int p[1001];
	
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T,n,cont;
	cin>>T;


	h[0]='0';h[1]='1';h[2]='2';h[3]='3';h[4]='4';h[5]='5';h[6]='6';h[7]='7';h[8]='8';h[9]='9';

	for(int i=1;i<=T;i++)
	{
		cin>>n>>v;
		cont=0;
		for(int j=0;j<=n;j++)
		{
			for(int k=0;k<=9;k++)
			{
				if(v[j]==h[k])
				{
					p[cont]=k;
				}
			}
			cont=cont+1;
		}
		int pp=0,pl=0,l;
		pp=p[0];
		for(int t=1;t<cont;t++)
		{
			if(t<=pp)
	        {
			   pp=pp+p[t];
	    	}
		    else
		    {
			   l=1;
			   pl=pl+l;
			   pp=pp+l+p[t];
		    }
		}
		cout<<"Case #"<<i<<": "<<pl<<endl;

	}

	return 0;
}
