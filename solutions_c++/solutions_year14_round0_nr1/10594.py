#include<iostream>
#include<stdlib.h>
#include<stdio.h>

using namespace std;

int main()
{   
   
    freopen("C:/Users/Akanksha/Downloads/A-small-attempt2.in","r",stdin);
    freopen("C:/Users/Akanksha/Downloads/A-small-attempt2.out","w",stdout);
	int t,i,j,match,matchi,k;
	cin>>t;
	k=0;
	int a[4][4];
	int b[4][4];
	int x1,x2;
	while(k<t)
	{    match=0;matchi=0;
		cin>>x1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			cin>>a[i][j];
		}
		cin>>x2;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			cin>>b[i][j];
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[x1-1][i]==b[x2-1][j])
				{
					match++;
					matchi=a[x1-1][i];
				}
			}
		}
		if(match==1)
		{
			cout<<"Case "<<"#"<<k+1<<": "<<matchi;
			cout<<endl;
		}
		if(match==0)
		{
			cout<<"Case "<<"#"<<k+1<<": Volunteer cheated!";
			cout<<endl;
		}
		if(match>1)
		{
			cout<<"Case "<<"#"<<k+1<<": Bad magician!";
			cout<<endl;
		}
		k++;
	}
	fclose(stdin);
	fclose(stdout);
}
