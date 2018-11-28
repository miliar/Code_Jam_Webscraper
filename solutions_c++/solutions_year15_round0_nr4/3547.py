#include <bits/stdc++.h>
#define ll long long 
#define maxn 100005
using namespace std;

string f(int r,int c,int x){
	       if((r*c)%x!=0)
		{
			return "RICHARD";
		}	
		else 
		{
			if(x<=2)
			{
				return "GABRIEL";
			}
			else if(x==3)
			{
				if((r*c)==3)
				{
					return "RICHARD";
				}
				else
				{
				return "GABRIEL";
				}
			}
			else if((r*c)==4 || (r*c)==8)
			{
			return "RICHARD";
			}
			else if((r*c)==12 || (r*c)==16)
			{
			  return "GABRIEL";
			}
		}
}
int main()
{
	int t;
        int x,r,c;
	cin>>t;
	int m=1;
	while(t--)
	{
		cin>>x>>r>>c;
	        cout<<"Case #"<<m<<": "<<f(r,c,x)<<"\n";
		m++;
	}
	return 0;
}
