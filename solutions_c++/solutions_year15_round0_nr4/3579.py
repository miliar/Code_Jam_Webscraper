#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("out_D.txt","w",stdout);
	long t;
	char rc[10]="RICHARD",g[10]="GABRIEL";
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(x==1)
			cout<<"Case #"<<i<<": "<<g<<endl;
		if(x==2)
		{
			if((r*c)%2==0)
              cout<<"Case #"<<i<<": "<<g<<endl;
            else
    		  cout<<"Case #"<<i<<": "<<rc<<endl;
		}
		if(x==3)
        {
            if(((r*c)%3==0)&&((r*c)>3))
                cout<<"Case #"<<i<<": "<<g<<endl;
            else
                cout<<"Case #"<<i<<": "<<rc<<endl;
        }
        
        if(x==4)
        {
                if(((r*c)==12)||((r*c)==16))
                    cout<<"Case #"<<i<<": "<<g<<endl;
                else
                     cout<<"Case #"<<i<<": "<<rc<<endl;
    	}
		
	}
}
