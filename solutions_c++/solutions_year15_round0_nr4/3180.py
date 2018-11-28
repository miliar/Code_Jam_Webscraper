#include <iostream>
using namespace std;
int main()
{
	int t,j=1,x,r,c,k;
	cin>>t;
	while(j<=t)
	{
		cin>>x>>r>>c;
		k=r*c;
		if(x>k)
		{
			cout<<"Case #"<<j<<": RICHARD"<<endl;
		}
		else if(x==k)
		{
			if(((r==1)&&(c==1)))
			{
				cout<<"Case #"<<j<<": GABRIEL"<<endl;	
			}
			else if((r==1)&&(c==2))
			{
				cout<<"Case #"<<j<<": GABRIEL"<<endl;
			}
			else if((r==2)&&(c==1))
			{
				cout<<"Case #"<<j<<": GABRIEL"<<endl;
			}
			else
			{
				cout<<"Case #"<<j<<": RICHARD"<<endl;
			}
		}
		else if(x<k) 
		{
			if(k%x==0)
			{
				if(x==4)
				{
					if((c==4)&&(r==2))
					{
						cout<<"Case #"<<j<<": RICHARD"<<endl;
					}
					else if((c==2)&&(r==4))
					{
						cout<<"Case #"<<j<<": RICHARD"<<endl;
					}
					else if((c==2)&&(r==2))
					{
						cout<<"Case #"<<j<<": RICHARD"<<endl;
					}
					else
					{
						cout<<"Case #"<<j<<": GABRIEL"<<endl;
					}
				}
				else
					{
						cout<<"Case #"<<j<<": GABRIEL"<<endl;
					}
				}
			else 
			{
				cout<<"Case #"<<j<<": RICHARD"<<endl;
			}
		}
		j++;
	}
	return 0;
}