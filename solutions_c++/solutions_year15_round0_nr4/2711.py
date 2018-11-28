#include<iostream>
using namespace std;
int main()
{
freopen("D-small-attempt1.in","r",stdin);
freopen("outp.in","w",stdout);
int n;
cin>>n;
for(int j=1;j<=n;j++)
{
int a,b,c;
cin>>a>>b>>c;
int hero;
switch(a)
	    {
	        case 1:
	                hero=1;
					break;
	        case 2:
	                if(b==1&&c==1||b==1&&c==3||b==3&&c==1||b==3&&c==3)
	                    hero=0;
	                else
	                    hero=1;
						break;
	        case 3:
	                if(b==1||c==1)
	                    hero=0;
	                else if(b==3||c==3)
	                    hero=1;
	                else
	                    hero=0;
						break;
	        case 4:
	                if(b==4&&c==4||b==4&&c==3||b==3&&c==4)
	                    hero=1;
	                else 
	                    hero=0;
	    }
if(hero==0)
cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
else
cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;	
}
return 0;
}
