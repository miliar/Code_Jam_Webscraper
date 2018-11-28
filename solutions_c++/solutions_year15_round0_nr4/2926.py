#include <iostream>
using namespace std;

int winBy(int x ,int r ,int c) {
	if (x == 1)
		return 1;
	if(x==2)
    {
        if((r*c)%2 == 0)
            return 1;
        else
            return 0;
    }
    if(x==3)
    {
        if(((r*c)%3==0)&&((r*c)>3))
            return 1;
        else
            return 0;   
    }

    if(x==4)
    {
        if(((r*c)==12)||((r*c)==16))
            return 1;
        else
            return 0;
    }
}

int main() 
{
	freopen("mn.in","r",stdin);
	freopen("out1.out","w",stdout);
	int test = 0;
	cin>>test;
	for (int i = 0; i < test; )
	{
		int x ,r , c;
		cin>>x>>r>>c;
		if (winBy(x,r,c) == 1)
		{
			cout<<"Case #"<<(++i)<<": GABRIEL"<<endl;	
		}
		else 
		{
			cout<<"Case #"<<(++i)<<": RICHARD"<<endl;
		}		
	}
}