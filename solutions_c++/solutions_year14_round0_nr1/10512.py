#include<iostream>
using namespace std;
int main()
{freopen("A-small-attempt1.in","r",stdin);
freopen("out.txt","w",stdout);
	int t=0,a[4][4],b[4][4],l1,l2,i,j,c,n,T;
	cin>>T;
	do
	{
		c=0;
		cin>>l1;
		for(i=0;i<4;i++)
		{
			
				for(j=0;j<4;j++)
			  	cin>>a[i][j];
			
			
		}
		cin>>l2;
		for(i=0;i<4;i++)
		{
			
				for(j=0;j<4;j++)
			  	cin>>b[i][j];
			
			
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[l1-1][i]==b[l2-1][j])
				{
					c++;n=a[l1-1][i];
				}
			}
		}
		if(c==1)
		{
			cout<<"case #"<<t+1<<": "<<n<<endl;
		}
		else{
			if(c==0)
			{
				cout<<"case #"<<t+1<<": Volunteer cheated!\n";	
			}
			else
				cout<<"case #"<<t+1<<": Bad magician!\n";
		}
		t++;
	}while(t!=T);
	return 0;
}


