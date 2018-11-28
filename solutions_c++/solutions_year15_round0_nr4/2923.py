#include<iostream>
using namespace std;
int main()
{
	freopen("D-small.in","r",stdin);
    freopen("D-small.out","w",stdout);
	int t;
	scanf("%d",&t);
	int cases  = 0;
	while(t--)
	{
	     cases++;
	     int n;
	     cin>>n;
	     int x, y;
	     cin>>x>>y;
	     if(n==1)
	     {
	     	cout<<"Case #"<<cases<<": GABRIEL"<<endl;
	     }
	     else if(n==2)
	     {
	     	if(x%2!=0 && y%2!=0)
	     	{
	     		cout<<"Case #"<<cases<<": RICHARD"<<endl;
	     	}
	     	else
	     	{
	     		cout<<"Case #"<<cases<<": GABRIEL"<<endl;
	     	}
	     }
	     else if(n==3)
	     {
	     	if( (y==3 && x!=1) || (x==3 && y==2) || (x==3 && y==4))
	     	{
	     		cout<<"Case #"<<cases<<": GABRIEL"<<endl;
	     	}
	     	else
	     	{
	     		cout<<"Case #"<<cases<<": RICHARD"<<endl;
	     	}
	     }
	     else if(n==4)
	     {
	     	if(x==4 && (y==3 || y==4 )  || (x==3 && y==4))
	     	{
	     			cout<<"Case #"<<cases<<": GABRIEL"<<endl;
	     	}
	     	else
	     	{
	     		cout<<"Case #"<<cases<<": RICHARD"<<endl;
	     	}
	     }
			 	
	}
	return  0;
}
