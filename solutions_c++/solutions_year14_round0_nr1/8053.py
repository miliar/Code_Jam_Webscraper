#include<iostream>

using namespace std;
int main()
{
	int a[5][5],b[5][5];
	int t,x,y,tmp=0,tot=0,num=0,count=0;
	cin>>t;
	while(t-->0)
	{
		int i,j;
		count++;
		cin>>x;
		for( i=1;i<5;++i)
		for(j=1;j<5;++j)
		cin>>a[i][j];
		
		
		
		cin>>y;
		for(i=1;i<5;++i)
		for(j=1;j<5;++j)
		cin>>b[i][j];
		
		
			tot=0;
			for(i=1;i<5;++i)
			{
				tmp=a[x][i];
				for(j=1;j<5;++j)
				{
					if(tmp==b[y][j])
					{num=tmp;
					tot++;
					}
				}
			}
			if(tot==1)
			cout<<"case #"<<count<<": "<<num<<'\n';   //
			
			else
			if(tot==0)
			cout<<"case #"<<count<<": Volunteer cheated!\n";
			
			else
			cout<<"case #"<<count<<": Bad magician!\n";	
		
	}
	return 0;
}
