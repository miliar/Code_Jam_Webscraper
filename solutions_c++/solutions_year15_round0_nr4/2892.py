#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int x,r,c;
        string ans;
        cin>>x>>r>>c;
        if(r>c)
        {
               swap(r,c);
        }
		if(x==1)
		{
			ans="GABRIEL\n";
		}
		else if(x==2)
		{
			if((c==3&&r==3)||(r==1&&(c==1||c==3)))
				ans="RICHARD\n";
			else ans="GABRIEL\n";
		}
		else if(x==3)
		{
			if((r==2&&c==3)||(r==3&&(c==3||c==4)))
				ans="GABRIEL\n";
			else ans="RICHARD\n";
		}
		else if(x==4)
		{
			if(c==4&&(r==3||r==4))
				ans="GABRIEL\n";
			else ans="RICHARD\n";
		}
    	cout<<"Case #"<<j<<": "<<ans;
    }
    return 0;
}
