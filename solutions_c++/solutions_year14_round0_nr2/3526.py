#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
		freopen("B-large.in","r",stdin);
		freopen("output.txt","w",stdout);
		int t,t1=0;
	    double c,f,x,p,p1,x1,x2,x3,a;
		scanf("%d",&t);
		while(t--)
		{
			t1++;
			cin>>c>>f>>x;
	//		cout<<c<<" "<<f<<" "<<x<<endl;
			
			if(x<=c)
			{
				printf("Case #%d: %.7f\n",t1,x/2);
			}
			else
			{
				p=f; a=2; p1=p+a;
				x1=c/a; x2=x/p1; x3=x/a;
				while(1)
				{
					if(x1+x2 <= x3)
					{
						x3=x1+x2;
						p1=p1+p;
						x2=x/p1;
						a=a+p;
						x1=x1+(c/a);
					}
					else
					{
						printf("Case #%d: %.7f\n",t1,x3);
						break;
					}
					
				}
				
			}
				
			
		}
		return 0;
}
