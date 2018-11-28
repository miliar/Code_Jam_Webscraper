#include<iostream>
using namespace std;
int main()
{
    int a[4][4],b[4][4],x,y,t,c=0,temp,m,i,j,k,l;
    cin>>t;
    for(m=0;m<t;m++)
    {
        c=0;
	
	cin>>x;
	for(i=0;i<4;i++)
	{
	for(j=0;j<4;j++)
	{cin>>a[i][j];
	}
    }
	cin>>y;
	for(i=0;i<4;i++)
	{
	
	for(j=0;j<4;j++)
	{cin>>b[i][j];
	}
    }
	
	for(k=0;k<4;k++)
	{for(l=0;l<4;l++)
	{if(a[x-1][k]==b[y-1][l])
	{temp=a[x-1][k];
	c++;
    }  
	}
	    
	}
	if(c==0)
	{cout<<"Case #"<<m+1<<": Volunteer Cheated!"<<endl;
	}
	else if(c>1)
	{cout<<"Case #"<<m+1<<": Bad Magician!"<<endl;
	}
    else
	{cout<<"Case #"<<m+1<<": "<<temp<<endl;
	}
}
return 0;
	
}
