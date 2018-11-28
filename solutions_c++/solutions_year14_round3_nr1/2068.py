#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{
	int t,p,q,i,count;
	cin>>t;
	for(i=1;i<=t;i++)
	{
	   cin>>p;
	   char c=getchar();
	   cin>>q;
	   double ck=log2((double)q);
	   int ch=(int)log2((double)q);
	   if(ck-ch>0)
	     cout<<"Case #"<<i<<": impossible"<<endl;
	   else
	   {
			count=0;
			while(p/q<1)
			{
				count++;
				p*=2;
			}
		    cout<<"Case #"<<i<<": "<<count<<endl;
		}
	}
	return 0;
}
