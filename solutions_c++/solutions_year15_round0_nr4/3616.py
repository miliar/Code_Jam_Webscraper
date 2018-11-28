#include <iostream>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int test,flag,i;
	cin>>test;
	for(i=1;i<=test;i++)
	{
		int x,r,c;
		cin>>x>>r>>c;
        if(x==1)
            flag=1;
        else if(x==2)
        {
            if((r==1&&c==1)||(r==1&&c==3)||(r==3&&c==1)||(r==3&&c==3))
                flag=2;
            else
                flag=1;
        }
        else if(x==3)
        {
            if((r==1||c==1)||(c==2&&r==2)||(r==2&&c==4)||(r==4&&c==2)||(r==4&&c==4))
                flag=2;
            else
                flag=1;
        }
        else if(x==4)
        {
            if((r==3&&c==4)||(r==4&&c==3)||(r== 4&&c== 4))
                flag=1;
            else
                flag=2;
        }
        if(flag==1)
            cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
        else if(flag==2)
            cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
	}
	return 0;
}
