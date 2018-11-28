#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int i,j,final,c=0,test,d=0,l=0,n,x=0;;
	cin>>test;
	double nam[1004],ken[1002];
	double l1[1004],l2[1004];
	while(test--)
	{
		++l;
		c=0;
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>nam[i];
			l1[i]=nam[i];
		}
		for(i=0;i<n;i++)
		{
			cin>>ken[i];
			l2[i]=ken[i];
		}
		sort(nam,nam+n);
		sort(ken,ken+n);
        sort(l1,l1+n);
        sort(l2,l2+n);
	/*	for(i=0;i<n;i++)
{
cout<<nam[i]<<" ";

	}cout<<"\n";
		for(i=0;i<n;i++)
{
cout<<ken[i]<<" ";

	}cout<<"\n";
*/
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(l1[j]>l2[i])
				{
					c++;
					l1[j]=0.0;
					break;
				}
			}
		}
		d=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(ken[j]>nam[i])
				{
					d++;
					ken[j]=0.0;
					break;
				}
			}
		}
		final=n-d;
		cout<<"Case #"<<l<<": "<<c<<" "<<final<<"\n";
	}
	return 0;
}